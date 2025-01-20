## Описание проекта

Автоматизация тестирования главной страницы сайта effective-mobile.ru.

## Автор

Бондаренко Алексей Олегович
- Telegram: [@alovsemprivet](https://t.me/alovsemprivet)
- GitHub: [Pr1ority](https://github.com/Pr1ority)

## Технологический стек

- Тестирование: Playwright, Allure, Pytest
- Контейнеризация: Docker
- Язык программирования: Python 3

## Как развернуть репозиторий

1. Клонируйте репозиторий
```bash
git clone https://github.com/Pr1ority/effective_tests.git
```
2. Перейдите в корневую директорию
```bash
cd effective_tests
```
3. Настройте виртуальное окружение
```bash
python -m venv venv
```
Для macOS/Linux
```bash
source venv/bin/activate
```
Для Windows
```bash
source venv/Scripts/activate
```
4. Выполните команду
```bash
docker build -t test-runner .
```
5. Запуск тестов в Docker
```bash
docker run --rm test-runner
```
6. Запуск тестов локально
```bash
pip install -r requirements.txt
```
```bash
pytest --alluredir=allure-results
```
7. Просмотр отчетов Allure
```bash
allure serve allure-results
```
