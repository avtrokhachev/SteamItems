import typing as tp

from sqlalchemy import CursorResult, Engine, create_engine


class Repository:
    _engine: tp.Optional[Engine] = None

    @classmethod
    def get_engine(cls) -> Engine:
        if cls._engine is None:
            cls._engine = create_engine(
                "postgresql://localhost:5432/avtrokhachev"
            )

        return cls._engine

    @classmethod
    def run(cls, *args, **kwargs) -> CursorResult:
        engine = cls.get_engine()
        with engine.begin() as conn:
            result = conn.execute(*args, **kwargs)

        return result
