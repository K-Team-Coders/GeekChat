FROM python:3.11

COPY ./telegramBot/requirements.txt .

RUN [ "pip", "install", "--upgrade", "pip"]

RUN [ "pip", "install", "-r", "requirements.txt"]

COPY . .

EXPOSE 12345

CMD ["python", "./telegramBot/tg_bot.py"]