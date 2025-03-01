from uuid import UUID

from fastapi import HTTPException
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import CookieParameters, SessionCookie
from fastapi_sessions.session_verifier import SessionVerifier

from pydantic import BaseModel

from app.core.config import cfg


class SessionData(BaseModel):
    """
    СТРУКТУРА ДАННЫХ ОПИСЫВАЮЩАЯ ОБЪЕКТ СЕССИИ.
    В НЕМ ХРАНИТСЯ ВСЯ НЕОБХОДИМЫЕ ДЛЯ РАБОТЫ СЕРВИСА ДАННЫЕ.
    """
    user_id: int
    refresh_token: str

cookie_params = CookieParameters()
cookie = SessionCookie(
    cookie_name=cfg.session.cookie_name,
    identifier="general_verifier",
    auto_error=True,
    secret_key=cfg.session.secret_key,
    cookie_params=cookie_params,
)

session_backend = InMemoryBackend[UUID, SessionData]()

class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True


verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=session_backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)
