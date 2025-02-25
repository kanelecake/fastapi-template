[Русская версия](./README_RU.md)

---

# FastAPI Project Template

## Description

This project is a template for FastAPI web applications. It includes a directory structure that ensures clean architecture, supports database migrations, caching, logging, and authentication.

## Project Structure


```
project_root/
├── app/                # Core modules (configuration, database, cache, CLI)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── cache.py
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── database.py
│   ├── models/         # Database model definitions
│   ├── routers/        # API routers
│   │   ├── endpoints/  # Main API endpoints
│   │   ├── schemas/    # Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   ├── v1.py
│   ├── services/       # Business logic
│   ├── utils/          # Utility functions (logging, caching, encryption, etc.)
│   │   ├── __init__.py
│   │   ├── formatter.py
│   │   ├── hashing.py
│   │   ├── logging.py
│   │   ├── response.py
│   │   ├── sessions.py
│   ├── main.py         # Application entry point
├── configs/            # Configuration files
├── data/               # Directory for storing data (if needed)
├── migrations/         # Database migrations (Alembic)
├── .gitignore          # Git ignored files
├── alembic.ini         # Alembic configuration
├── README.md           # Project description
├── requirements.txt    # Project dependencies
```


## Installation

1. Clone the repository:
   ```bash
   git clone <repository_URL>
   cd <project_name>
   ```


2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS and Linux
   venv\Scripts\activate     # For Windows
   ```


3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Configure project

Edit file `configs/app.yaml` (remove an example postfix example)
and fill by your db and cache credentials.

## Running the Project

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

   The server will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

2. Open the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Database Migrations

The project uses Alembic for managing database migrations.

1. Create a new migration:
   ```bash
   alembic revision --autogenerate -m "initial migration"
   ```


2. Apply migrations:
   ```bash
   alembic upgrade head
   ```

## License

This project is distributed under the MIT License.
