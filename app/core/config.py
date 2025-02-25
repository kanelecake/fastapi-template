import pathlib

import yaml

from pydantic import BaseModel, Field, MySQLDsn
from pydantic_settings import BaseSettings
from app.core.cli import cli_args


# Классы для различных частей конфигурации
class Cache(BaseModel):
    # Адрес сервиса кеширования
    host: str
    # Порт сервиса кеширования
    port: int
    # База данных в сервисе кеширования
    db: int = 0


class Session(BaseModel):
    # Название сессионной куки
    cookie_name: str
    # Секретный ключ для сессионной куки
    secret_key: str

class GZip(BaseModel):
    # Минимальный размер
    minimum_size: int = 5000
    # Уровень сжатия
    level: int = Field(ge=1, le=9, default=5)


class DefaultAdminCredentials(BaseModel):
    # Имя администратора
    username: str
    # Пароль администратора
    password: str = Field(min_length=8)


# Модель настроек, которая наследуется от BaseSettings
class Settings(BaseSettings):
    # Режим отладки
    debug: bool = Field(default=True)
    # Строка подключения к базе данных
    dsn: MySQLDsn = Field(alias="dsn")
    # Путь до файла логирования
    log_file: str = Field(alias="log_file")
    # Массив разрешенных доменов
    allowed_domains: list[str] = Field(alias="allowed_domains")
    # Кеширование
    cache: Cache = Field(alias="cache")
    # Сессия пользователя
    session: Session = Field(alias="session")
    # Стандартные настройки для аккаунта администратора
    admin_credentials: DefaultAdminCredentials = Field(alias="admin_credentials")
    # Настройка gzip для запросов
    compress: GZip = Field(alias="compress")

    class Config:
        # Путь до файла YAML будет передан через путь к файлу
        settings_sources = []


# Чтение и загрузка данных из YAML
yaml_file_path = pathlib.Path(__file__).parent.parent.parent / cli_args.config

print("----- CONFIGURATION INIT -----")
print("Start to load a config file...")
with open(yaml_file_path, "r") as file:
    yaml_data = yaml.safe_load(file)
    print("1/2. File is loaded successfully.")

# Инициализация настроек с использованием данных из YAML
cfg = Settings.parse_obj(yaml_data)

print("2/2. Config is parsed successfully.")
print("Config is loaded successfully!")
print("----- CONFIGURATION COMPLETE -----")
