import json
import socket
import telebot
from loguru import logger

TOKEN = '7102875827:AAESUKPylyhN36SmZlD22X3WlGVqfpEdWEg'

bot = telebot.TeleBot(TOKEN)

logger.success('telega is started')



@bot.message_handler(commands=['start'])
def start(message):
    # ID АДМИНА, которому будет отправлено сообщение
    admin_id = message.from_user.id
# НАДО ПЕРЕДАТЬ ЗНАЧЕНИЕ ПЕРЕМЕННОЙ ИЗ ФУНКЦИИ START В ФУНКЦИЮ HANDLE_CLIENT ДЛЯ ОТПРАВКИ УВЕДОМЛЕНИЯ ПОЛЬЗОВАТЕЛЮ

def handle_client(client_socket):
    # Получение JSON файла от сокета
    data = client_socket.recv(1024)
    try:
        json_data = json.loads(data.decode('utf-8'))
        # Отправка сообщения пользователю
        bot.send_message(admin_id, json_data['message'])
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345)) # Пример адреса и порта
    server_socket.listen(1)
    print("Сервер запущен, ожидание подключений...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключение от {addr}")
        handle_client(client_socket)
        client_socket.close()

if name == "main":
    start_server()

bot.polling(non_stop=True)