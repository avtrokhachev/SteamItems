import typing as tp

from sqlalchemy import CursorResult, Engine, create_engine
from common.concepts import config


class Repository:
    _engine: tp.Optional[Engine] = None

    @classmethod
    def get_engine(cls) -> Engine:
        if cls._engine is None:
            cls._engine = create_engine(config.get_value("database.connection_url"))

        return cls._engine

    @classmethod
    def run(cls, *args, **kwargs) -> CursorResult:
        engine = cls.get_engine()
        with engine.begin() as conn:
            result = conn.execute(*args, **kwargs)

        return result
