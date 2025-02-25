import logging

from app.core.config import cfg

# Настройка логирования
logging.basicConfig(level=logging.DEBUG if cfg.debug else logging.INFO,
                    filename=cfg.log_file, filemode="w", format="[%(asctime)s %(levelname)s]: %(message)s")
logger = logging.getLogger(__name__)


# Декоратор для логирования ошибок с путём до функции
def enable(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
    return wrapper

async def enable_async(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
    return wrapper