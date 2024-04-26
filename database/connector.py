import os
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import create_engine
from model import *
from loguru import logger




def connect_database():
    try:
        # Загрузка переменных среды из файла .env
        load_dotenv()

        # Получение параметров для подключения к базе данных из переменных среды
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_name = os.getenv("DB_NAME")
        # Создаем экземпляр engine для подключения к базе данных PostgreSQL
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}', echo=True)

        # Создаем таблицы в базе данных, если они еще не созданы
        Base.metadata.create_all(engine)

        # Создаем сессию
        Session = sessionmaker(bind=engine)
        session = Session()
        logger.success(f"Successfully connected to session with credential: {db_user}:{db_password}@{db_host}/{db_name}")
        return session
    except Exception as e:
        logger.error(str(e))
