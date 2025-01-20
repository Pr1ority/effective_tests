# Используем образ Python
FROM python:3.10-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем pip и Playwright
RUN pip install --upgrade pip && \
    pip install playwright

# Устанавливаем зависимости Playwright
RUN playwright install --with-deps

# Копируем файлы проекта
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Playwright
RUN playwright install

# Копируем исходный код
COPY . .

# Запуск тестов
CMD ["pytest", "--alluredir=allure-results"]