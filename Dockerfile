# Определяем базовый образ
FROM python:3.10.2-slim-bullseye

# Установка переменных окружения
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории
WORKDIR /my_site

# Установка зависимостей
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Исходный код проекта Django копируется из локального каталога в каталог образа.
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
