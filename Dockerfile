FROM python:3.11

# set current directory for work
# устанавливаем рабочий каталог
WORKDIR ./

# copy file requirements.txt to workdir
# Копируем файл зависимостей в рабочую директорию внутри контейнера
COPY ./pyproject.toml ./pyproject.toml

# Run pip and install requiremnts withous localy saved
# Устанавливаем зависимости и не сохраняем их локально
RUN pip install --no-cache-dir --upgrade poetry \
    && poetry config virtualenvs.create false \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

# Copy project file to work directory
# Копируем файлы для работы

COPY fastApi .
COPY notebooks .
COPY database .
# Run
# Запускаем проект

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "fastApi.main:app", "--bind", "0.0.0.0:8080"]