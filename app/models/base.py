from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime, MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr, Session

from app.utils.formatter import pluralize, utc_to_local

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    __abstract__ = True  # Помечаем таблицу как абстрактная, чтобы избежать ее создания

    metadata = MetaData(naming_convention=convention)

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True, default=None)

    @declared_attr
    def __tablename__(self):
        """ Отвечает за форматирование таблиц базы данных в определенный формат """
        snake_case = ''.join(['_' + c.lower() if c.isupper() else c for c in self.__name__]).lstrip('_')
        return f'iam_{pluralize(snake_case)}'

    def soft_delete(self, session: Session):
        """ Помечаем запись как удаленную, установив self.deleted_at текущей utc метке """
        self.deleted_at = datetime.now()
        session.commit()

    def _get_timestamps(self):
        created_at = utc_to_local(self.created_at)
        updated_at = utc_to_local(self.updated_at)

        return {
            'created_at': created_at.strftime('%d.%m.%Y, %H:%M:%S'),
            'updated_at': updated_at.strftime('%d.%m.%Y, %H:%M:%S'),
        }

    def _to_dict(self) -> dict:
        """Базовая реализация, предоставляющая стандартные поля."""
        return {
            "id": self.id,
            **(self._get_timestamps()),
        }
