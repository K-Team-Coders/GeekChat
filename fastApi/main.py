import asyncio
import json
import socket
import uuid
from datetime import datetime
from typing import Dict, List

import uvicorn
from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from helper_funcion import *
from notebooks.toxicity import toxicityAnalisis

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Структура данных для хранения комнат, пользователей и сообщений
rooms: Dict[str, Dict[str, List[str]]] = {}
metrics_history: Dict[str, Dict[str, List[float]]] = {}
room_websockets: Dict[str, List[WebSocket]] = {}

# Структура данных для хранения пользователей и их токенов
users: Dict[str, str] = {}


async def save_messages():
    while True:
        await asyncio.sleep(60)  # Подождать 60 секунд
        current_time = datetime.now()
        for room_id, room_data in rooms.items():
            messages = room_data.get("messages", [])
            # Сохранение сообщений с временной меткой в формате "час:минута:секунда"
            message_with_timestamp = [f"{current_time.strftime('%H:%M:%S')} - {msg}" for msg in messages]
            with open(f"messages_{room_id}.txt", "a") as file:
                file.write("\n".join(message_with_timestamp) + "\n")


threshold_activity = 0
threshold_mood = 0


async def check_activity_and_mood():
    while True:
        await asyncio.sleep(60)  # Подождать 60 секунд
        current_time = datetime.now()
        for room_id, room_data in rooms.items():
            users_count = len(room_data.get("users", []))
            messages_count = len(room_data.get("messages", []))

            for msg in room_data.get("messages", []):
                if toxicityAnalisis(msg) == 1:
                    await send_notification("Агрессивное поведение пользователей в комнате номер: {}".format(room_id))

            positive_count = sum(
                1 for msg in room_data.get("messages", []) if score_calculate_emotion_coloring(msg) == 1)
            negative_count = sum(
                1 for msg in room_data.get("messages", []) if score_calculate_emotion_coloring(msg) == -1)
            # Проверка, чтобы избежать деления на ноль
            if messages_count == 0:
                activity = 0
                mood = 0
            else:
                activity = users_count / messages_count
                mood = (positive_count - negative_count) / messages_count
            # Обновление метрик
            if room_id not in metrics_history:
                metrics_history[room_id] = {"activity": [], "mood": []}
            metrics_history[room_id]["activity"].append(activity)
            metrics_history[room_id]["mood"].append(mood)

            # Отправка уведомления, если активность или настроение ниже пороговых значений
            if activity < threshold_activity:
                await send_notification("Низкая активность в комнате номер: {}".format(room_id))
            if mood < threshold_mood:
                await send_notification("Негативный настрой в комнате номер: {}".format(room_id))


async def send_notification(message):
    # Отправка сообщения через сокет
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))  # Пример адреса и порта сервера
        data = json.dumps({'message': message})
        client_socket.send(data.encode('utf-8'))
        client_socket.close()
    except Exception as e:
        logger.error(f"Error sending notification: {e}")


@app.websocket("/ws/{room_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, token: str):
    await websocket.accept()
    logger.info(f"WebSocket {room_id} connected")
    # Проверка наличия токена в заголовке
    logger.info(token)
    if token is None or token not in users:
        raise HTTPException(status_code=401, detail="Unauthorized")

    username = users[token]
    logger.info(f"User {username} connected")
    # Создание новой комнаты, если она еще не существует
    if room_id not in rooms:
        rooms[room_id] = {"users": [], "messages": [], "activity": 0, "mood": 0}
    if room_id not in room_websockets:
        room_websockets[room_id] = []
    room_websockets[room_id].append(websocket)
    # Добавление пользователя к комнате
    rooms[room_id]["users"].append(username)
    logger.debug(rooms)

    # Асинхронный цикл для получения данных из сокета
    async def handle_messages():
        try:
            async for data in websocket.iter_text():
                await websocket.send_text(
                    "{\"username\":" + "\"" + f"{username}" + "\"" + ", \"message\":" + "\"" + f"{data}" + "\"" + ", \"date\":" + "\"" + f"{datetime.now()}" + "\"" + "}")
                logger.debug(data)
                for ws in room_websockets.get(room_id, []):
                    logger.debug(ws)
                    if ws != websocket:
                        await ws.send_text(
                            "{\"username\":" + "\"" + f"{username}" + "\"" + ", \"message\":" + "\"" + f"{data}" + "\"" + ", \"date\":" + "\"" + f"{datetime.now()}" + "\"" + "}")
                # Сохранение сообщения для соответствующей комнаты
                rooms[room_id]["messages"].append(f"{username}: {data}")
        finally:
            if room_id in room_websockets:
                room_websockets[room_id].remove(websocket)

    # Запускаем обработку сообщений в отдельном потоке

    await asyncio.gather(handle_messages())
    await asyncio.gather(save_messages())
    await asyncio.gather(check_activity_and_mood())


@app.get("/register")
async def register_user():
    # Генерация уникального токена пользователя
    token = str(uuid.uuid4())
    # Сохранение токена в структуре пользователей
    users[token] = token
    return {"token": token}


@app.get("/rooms")
async def get_rooms():
    # Получение списка комнат
    return list(rooms.keys())


@app.get("/rooms/{room_id}/users")
async def get_room_users(room_id: str):
    # Получение списка пользователей в комнате
    return rooms.get(room_id, {}).get("users", [])


@app.get("/rooms/{room_id}/messages")
async def get_room_messages(room_id: str):
    # Получение всех сообщений комнаты
    return rooms.get(room_id, {}).get("messages", [])


@app.get("/rooms/{room_id}/activity")
async def get_room_activity(room_id: str):
    # Получение активности комнаты
    return rooms.get(room_id, {}).get("activity", 0)


@app.get("/rooms/{room_id}/mood")
async def get_room_mood(room_id: str):
    # Получение настроения комнаты
    return rooms.get(room_id, {}).get("mood", 0)


@app.get("/rooms/{room_id}/activity/history")
async def get_room_activity_history(room_id: str):
    # Получение истории активности комнаты
    return metrics_history.get(room_id, {}).get("activity", [])


@app.get("/rooms/{room_id}/mood/history")
async def get_room_mood_history(room_id: str):
    # Получение истории настроения комнаты
    return metrics_history.get(room_id, {}).get("mood", [])


if __name__ == '__main__':
    uvicorn.run("fastApi.main:app", host='0.0.0.0', port=8000)
