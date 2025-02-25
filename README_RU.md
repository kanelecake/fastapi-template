# FastAPI Project Template

[Русская версия](./README_RU.md)

## Описание

Этот проект является шаблоном для веб-приложений на FastAPI. Он включает в себя структуру директорий, обеспечивающую чистую архитектуру, поддержку миграций базы данных, кеширование, логирование и аутентификацию.

## Структура проекта
```
project_root/
├── app/                # Основные модули (конфигурация, база данных, кеш, CLI)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── cache.py
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── database.py
│   ├── models/         # Определение моделей базы данных
│   ├── routers/        # Роутеры API
│   │   ├── endpoints/  # Основные конечные точки API
│   │   ├── schemas/    # Схемы Pydantic
│   │   │   ├── __init__.py
│   │   │   ├── v1.py
│   ├── services/    # Логика бизнес-процессов
│   ├── utils/       # Утилитарные функции (логирование, кеширование, шифрование и т.д.)
│   │   ├── __init__.py
│   │   ├── formatter.py
│   │   ├── hashing.py
│   │   ├── logging.py
│   │   ├── response.py
│   │   ├── sessions.py
│   ├── main.py      # Точка входа в приложение
├── configs/         # Конфигурационные файлы
├── data/            # Директория для хранения данных (если требуется)
├── migrations/      # Миграции базы данных (Alembic)
├── .gitignore       
├── alembic.ini      # Конфигурация Alembic
├── README.md        # Описание проекта
├── requirements.txt # Зависимости проекта
```

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd <имя_проекта>
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для macOS и Linux
   venv\Scripts\activate     # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Конфигурация

Отредактируйте файл `configs/app.yaml` (стереть из названия example)
согласно данным используемым в вашем проекте.

## Запуск проекта
1. Запустите сервер FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```
   Сервер будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

2. Откройте документацию API:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Миграции базы данных
Проект использует Alembic для управления миграциями базы данных.
1. Создайте новую миграцию:
   ```bash
   alembic revision --autogenerate -m "initial migration"
   ```
2. Примените миграции:
   ```bash
   alembic upgrade head
   ```


## Лицензия
Этот проект распространяется под лицензией MIT.

