from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import Query

from app.core.config import cfg


class QueryWithSoftDelete(Query):
    def __new__(cls, *args, **kwargs):
        obj = super(QueryWithSoftDelete, cls).__new__(cls)
        with_deleted = kwargs.pop('_with_deleted', False)
        if len(args) > 0:
            super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
            return obj.filter_by(deleted_at=None) if not with_deleted else obj
        return obj

    def with_deleted(self):
        return self.__class__(self._only_full_mapper_zero('get'), _with_deleted=True)


# Подключаемся к базе данных
engine = create_async_engine(
    cfg.dsn,
    future=True,
    echo=True,
)

SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)


async def get_db():
    try:
        async with SessionLocal() as session:
            yield session
    finally:
        await session.close()


SessionDep: AsyncSession = Depends(get_db)