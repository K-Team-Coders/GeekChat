import time
from typing import Dict, List
from fastApi.pydantic_model import ChatMessage
from fastapi import WebSocket
from fastApi.helper_funcion import score_calculate_emotion_coloring


# Класс для хранилища сообщений чата
class ChatStorage:
    def __init__(self):
        self.storage: Dict[str, List[ChatMessage]] = {}

    def add_message(self, chat_id: str, message: ChatMessage):
        if chat_id not in self.storage:
            self.storage[chat_id] = []
        self.storage[chat_id].append(message)

    def get_messages(self, chat_id: str) -> List[ChatMessage]:
        return self.storage.get(chat_id, [])


# Класс для пула соединений
class ConnectionPool:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def acquire_connection(self, chat_id: str, websocket: WebSocket):
        if chat_id not in self.active_connections:
            self.active_connections[chat_id] = []

        await websocket.accept()
        self.active_connections[chat_id].append(websocket)
        return websocket

    async def release_connection(self, chat_id: str, websocket: WebSocket):
        self.active_connections[chat_id].remove(websocket)


class ConnectionPoolData:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}
        self.messages_count = 0
        self.users_count = 0
        self.positive_messages_count = 0
        self.negative_messages_count = 0
        self.activity = []
        self.retrospective_data = {"mood": [], "activity": []}


# Словарь для хранения данных о каждом пуле соединений
connection_pools_data: Dict[str, ConnectionPoolData] = {}


# Функция для обновления данных о пуле соединений
def update_pool_data(chat_id: str, message: ChatMessage):
    if chat_id not in connection_pools_data:
        connection_pools_data[chat_id] = ConnectionPoolData()

    current_time = time.time()

    # Обновляем данные активности
    connection_pools_data[chat_id].activity.append(
        (current_time, len(connection_pools_data[chat_id].active_connections)))
    message_mood = score_calculate_emotion_coloring(message.message)
    # Обновляем данные о настроении
    if message_mood == 1:
        connection_pools_data[chat_id].positive_messages_count += 1
    elif message_mood == -1:
        connection_pools_data[chat_id].negative_messages_count += 1

    # Добавляем данные в ретроспективное хранилище
    connection_pools_data[chat_id].retrospective_data["mood"].append((current_time, connection_pools_data[
        chat_id].positive_messages_count - connection_pools_data[chat_id].negative_messages_count))
    connection_pools_data[chat_id].retrospective_data["activity"].append(
        (current_time, len(connection_pools_data[chat_id].active_connections)))

