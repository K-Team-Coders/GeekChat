import asyncio
import uuid
from datetime import datetime
from typing import Dict, List
from loguru import logger
import uvicorn
from fastapi import FastAPI, WebSocket, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

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


async def check_activity_and_mood():
    while True:
        await asyncio.sleep(60)  # Подождать 60 секунд
        current_time = datetime.now()
        for room_id, room_data in rooms.items():
            users_count = len(room_data.get("users", []))
            messages_count = len(room_data.get("messages", []))
            positive_count = sum(
                1 for msg in room_data.get("messages", []) if "хорошо" in msg.lower() or "позитив" in msg.lower())
            negative_count = sum(
                1 for msg in room_data.get("messages", []) if "плохо" in msg.lower() or "негатив" in msg.lower())
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


# @app.on_event("startup")
# async def startup_event():
#     # Запустить сохранение сообщений и проверку активности и настроения
#     await asyncio.create_task(save_messages())
#     await asyncio.create_task(check_activity_and_mood())


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

    # Добавление пользователя к комнате
    rooms[room_id]["users"].append(username)
    logger.debug(rooms)
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"username:{username}, message:{data}, date:{datetime.now()}")
        logger.debug(data)
        # Сохранение сообщения для соответствующей комнаты
        rooms[room_id]["messages"].append(f"{username}: {data}")


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
