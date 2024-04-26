import os
import time
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DBenv = Path().cwd().parent.joinpath("DB.env")
load_dotenv(DBenv, override=True)

engine = 0

logger.debug("Waiting for DB service Up...")
time.sleep(5)

try:     
    PRODUCTION = os.environ.get("PRODUCTION")

    if PRODUCTION == 'True':
        PRODUCTION = True
    else:
        PRODUCTION = False

    HOST = None
    DBNAME = None
    PASSWORD = None

    if PRODUCTION:
        HOST=os.environ.get("DB_HOST")  
        DBNAME=os.environ.get("POSTGRES_DB")
        USER=os.environ.get("POSTGRES_USER")
        PASSWORD=os.environ.get("POSTGRES_PASSWORD")
    else:
        HOST=os.environ.get("DB_LOCAL")
        DBNAME=os.environ.get("LOCAL_DB")
        USER=os.environ.get("LOCAL_USER")
        PASSWORD=os.environ.get("LOCAL_PASSWORD")
    
    PORT=os.environ.get("PORT")

    logger.success(('Docker DB connection started \n', HOST, PORT, DBNAME, USER, PASSWORD, ' - env variables!'))

    engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DBNAME}")
    engine.connect()

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    base = declarative_base()

    if PRODUCTION:
        logger.success('Docker DB connected!')
    else:
        logger.success('Local DB connected!')

except Exception as e:
    logger.error(f'Database connect failed \n {e}!')
