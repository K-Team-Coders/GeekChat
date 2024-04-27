from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect, WebSocket
from fastapi.responses import HTMLResponse

from fastApi.pattern_model import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаем экземпляры хранилища сообщений и пула соединений
chat_storage = ChatStorage()
connection_pool = ConnectionPool()


# Роут для веб-сокета
@app.websocket("/chat/{chat_id}/{username}")
async def websocket_endpoint(chat_id: str, username: str, websocket: WebSocket):
    websocket_connection = await connection_pool.acquire_connection(chat_id, websocket)
    try:
        while True:
            data = await websocket_connection.receive_text()
            message = ChatMessage(username=username, message=data)
            update_pool_data(chat_id, message)
    except WebSocketDisconnect:
        await connection_pool.release_connection(chat_id, websocket_connection)


# Роут для получения данных о пуле соединений
@app.get("/pool/{chat_id}")
async def get_pool_data(chat_id: str):
    return connection_pools_data.get(chat_id, {})


# Роут для получения сообщений чата
@app.get("/chat/{chat_id}", response_model=List[ChatMessage])
async def get_chat_messages(chat_id: str):
    return chat_storage.get_messages(chat_id)


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


html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Chat</title>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <div id="messages"></div>
    <input type="text" id="messageInput" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button>

    <script>
        const session_id = "your_session_id"; // Replace with actual session ID
        const user_id = "your_user_id"; // Replace with actual user ID
        const ws = new WebSocket(`ws://localhost:8080/chat/${session_id}/${user_id}`);

        ws.onmessage = function(event) {
            const messagesDiv = document.getElementById("messages");
            const message = document.createElement("div");
            message.textContent = event.data;
            messagesDiv.appendChild(message);
        };

        function sendMessage() {
            const input = document.getElementById("messageInput");
            const message = input.value;
            ws.send(message);
            input.value = "";
        }
    </script>
</body>
</html>"""

if __name__ == '__main__':
    uvicorn.run("fastApi.main:app", host='0.0.0.0', port=8000)
