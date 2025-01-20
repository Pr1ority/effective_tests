# Используем образ Python
FROM python:3.10-slim

# Установка зависимостей системы

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Playwright
RUN pip install playwright && playwright install

#Копируем файлы проекта
WORKDIR /app
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt

# Запуск тестов
CMD ['pytest', 'alluredir=allure-results']