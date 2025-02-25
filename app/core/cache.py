import json
import redis

from datetime import timedelta
from typing import Any

from app.core.config import cfg
from app.utils import logging
from app.utils.response import json_error_response


cache = redis.Redis(host=cfg.cache.host, port=cfg.cache.port, db=cfg.cache.db, protocol=3)


@logging.enable_async
async def get_dict(key: str, err_code: str, err_desc: str) -> dict[str, Any]:
    """
    Метод используется для получения данных из кэша с парсингом JSON

    :param key: Ключ хранящийся в Cache.
    :param err_code: Код ошибки, который будет возвращен, если данные не будут найдены.
    :param err_desc: Описание ошибки, которое будет возвращен, если данные не будут найдены.
    :return:
    """
    data = cache.get(key)
    if data is None:
        raise json_error_response(404, err_code, err_desc)
    return json.loads(data)


@logging.enable_async
async def set_dict(key: str, data: dict, duration: timedelta):
    """
    Метод кодирует словарь в json и сохраняет в кеш.

    :param key: Ключ в Cache.
    :param data: Данные в виде словаря.
    :param duration: TTL данных.
    :return:
    """
    data = json.dumps(data)
    cache.setex(key, duration, data)
