from fastapi import FastAPI

from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.core.config import cfg
from app.routes.v1 import api_v1

app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=cfg.allowed_domains)

# Если окружение является production-ready, то включаем сжатие для запросов
if not cfg.debug:
    app.add_middleware(GZipMiddleware, minimum_size=cfg.compress.minimum_size, compresslevel=cfg.compress.level)

app.include_router(api_v1, prefix="/api/v1")