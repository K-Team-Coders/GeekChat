import asyncio
import time
from typing import Dict, List

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect, WebSocket
from fastapi.responses import HTMLResponse
from fastApi.helper_funcion import score_calculate_emotion_coloring
from fastApi.pydantic_model import SessionStatus, User
from database.connector import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# session = connect_database()


# Словарь для хранения информации о чатах
chat_rooms: Dict[str, Dict[str, any]] = {}

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Chat Test</title>
    <script>
        let ws = new WebSocket("ws://localhost:8080/chat/1/user1");

        ws.onopen = function(event) {
            console.log("WebSocket connection established.");
        };

        ws.onmessage = function(event) {
            let message = JSON.parse(event.data);
            console.log("Received message:", message);
            document.getElementById("mood").innerText = "Mood: " + message.mood;
            document.getElementById("activity").innerText = "Activity: " + message.activity;
        };

        ws.onerror = function(error) {
            console.error("WebSocket error:", error);
        };

        function sendMessage() {
            let messageInput = document.getElementById("messageInput");
            let message = messageInput.value;
            ws.send(message);
            messageInput.value = "";
        }
    </script>
</head>
<body>
    <h1>WebSocket Chat Test</h1>
    <div id="mood"></div>
    <div id="activity"></div>
    <input type="text" id="messageInput" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button>
</body>
</html>"""


async def calculate_activity(chat_id: str):
    last_calculation_time = time.time()
    while True:
        if chat_id in chat_rooms:
            current_time = time.time()
            elapsed_time = current_time - last_calculation_time
            if elapsed_time >= 60:
                # Расчет активности пользователей в чате
                total_message_count = chat_rooms[chat_id]["total_message_count"]
                activity = total_message_count / (elapsed_time / 60)
                logger.info(f"Activity in chat {chat_id}: {activity} messages per minute")

                last_calculation_time = current_time
                chat_rooms[chat_id]["total_message_count"] = 0
        await asyncio.sleep(1)


async def calculate_mood(chat_id: str):
    last_calculation_time = time.time()
    while True:
        if chat_id in chat_rooms:
            current_time = time.time()
            elapsed_time = current_time - last_calculation_time
            if elapsed_time >= 60:
                # Расчет настроения пользователей в чате
                total_message_count = chat_rooms[chat_id]["total_message_count"]
                positive_count = chat_rooms[chat_id]["positive_count"]
                negative_count = chat_rooms[chat_id]["negative_count"]
                if total_message_count > 0:
                    mood = (positive_count - negative_count) / total_message_count
                    logger.info(f"Mood in chat {chat_id}: {mood} messages per minute")
                else:
                    logger.info(f"Mood in chat {chat_id}: No messages")

                last_calculation_time = current_time
                chat_rooms[chat_id]["total_message_count"] = 0
                chat_rooms[chat_id]["positive_count"] = 0
                chat_rooms[chat_id]["negative_count"] = 0
        await asyncio.sleep(1)


@app.websocket("/chat/{chat_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str, user_id: str):
    await websocket.accept()

    # Добавляем чат, если его еще нет
    if chat_id not in chat_rooms:
        chat_rooms[chat_id] = {"start_time": time.time(), "total_message_count": 0, "positive_count": 0,
                               "negative_count": 0, "clients": []}

        await asyncio.create_task(calculate_activity(chat_id))
        await asyncio.create_task(calculate_mood(chat_id))

    async def send_mood_and_activity():
        while True:
            if chat_id in chat_rooms:
                total_message_count = chat_rooms[chat_id]["total_message_count"]
                logger.debug(total_message_count)
                positive_count = chat_rooms[chat_id]["positive_count"]
                negative_count = chat_rooms[chat_id]["negative_count"]
                logger.debug(positive_count)
                logger.debug(negative_count)
                activity = total_message_count / 60 if total_message_count > 0 else 0

                if total_message_count > 0:
                    mood = (positive_count - negative_count) / total_message_count
                    logger.debug(f"mood: {mood}")
                    await websocket.send_json({"mood": mood, "activity": activity})
                else:
                    await websocket.send_json({"mood": None, "activity": None})
            await asyncio.sleep(60)

    # Добавляем пользователя в список клиентов чата
    chat_rooms[chat_id][user_id].append(websocket)

    try:
        while True:
            # Получаем сообщение от пользователя
            data = await websocket.receive_text()
            logger.debug(data)
            # Увеличиваем счетчик сообщений для чата
            chat_rooms[chat_id]["total_message_count"] += 1

            # Вычисляем эмоциональную окраску сообщения
            emotion_score = score_calculate_emotion_coloring(data)
            logger.debug(f"emotional score: {emotion_score}")

            if emotion_score > 0:
                chat_rooms[chat_id]["positive_count"] += 1
            elif emotion_score < 0:
                chat_rooms[chat_id]["negative_count"] += 1
            await asyncio.create_task(send_mood_and_activity())
    except WebSocketDisconnect:
        # Удаляем пользователя из чата при отключении
        chat_rooms[chat_id][user_id].remove(websocket)
        logger.info(f"user with id: {user_id} successfully delete")


#
# @app.post("/status")
# async def start_session(request: SessionStatus):
#     if request.status == "start":
#         time_start = datetime.now()
#         new_session = Session(
#             session_id=request.session_id,
#             start_time=time_start,
#         )
#         session.add(new_session)
#         session.commit()
#         new_session_activity = SessionActivity(session_id=request.session_id)
#         session.add(new_session_activity)
#         session.commit()
#     elif request.status == "stop":
#         session_to_update = session.query(Session).filter_by(id=request.session_id).first()
#         time_end = datetime.now()
#         session_to_update.end_time = time_end
#         session.commit(session_to_update)
@app.get("/")
async def htm():
    return HTMLResponse(html)


if __name__ == '__main__':
    uvicorn.run("fastApi.main:app", host='0.0.0.0', port=8000)
