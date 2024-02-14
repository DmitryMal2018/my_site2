# Определяем базовый образ
FROM python:3.11.8-slim-bullseye

# Установка переменных окружения
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории
WORKDIR /my_site2

# Установка зависимостей
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Исходный код проекта Django копируется из локального каталога в каталог
# образа.
COPY . .

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"] 
