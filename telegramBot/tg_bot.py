import json
import os
import socket
import telebot
import asyncio
from loguru import logger
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

bot = telebot.TeleBot(TOKEN)

logger.success('Telegram bot is started')

# Список для хранения ID всех активных чатов
active_chats = set()


async def listen_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    logger.success("Socket server is started, waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        logger.success(f"Connection from {addr}")
        data = client_socket.recv(1024)
        try:
            json_data = json.loads(data.decode('utf-8'))
            # Отправка сообщения всем активным пользователям в Telegram
            for chat_id in active_chats:
                bot.send_message(chat_id, json_data['message'])
        except json.JSONDecodeError:
            logger.error("Error decoding JSON")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            client_socket.close()


@bot.message_handler(commands=['start'])
def start(message):
    # Добавление ID чата в список активных чатов
    active_chats.add(message.chat.id)
    logger.success('Chat ID {} added to active chats'.format(message.chat.id))


@bot.message_handler(commands=['stop'])
def stop(message):
    # Удаление ID чата из списка активных чатов
    active_chats.remove(message.chat.id)
    logger.success('Chat ID {} removed from active chats'.format(message.chat.id))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Создание задачи для асинхронной функции прослушивания сокета
    listen_task = loop.create_task(listen_socket())
    # Запуск бота
    bot.polling(none_stop=True)
