import typing as tp

import sqlalchemy
from sqlalchemy import CursorResult, Engine, create_engine

from common.concepts import config


class Repository:
    _engine: tp.Optional[Engine] = None

    @classmethod
    def get_engine(cls) -> Engine:
        if cls._engine is None:
            cls._engine = create_engine(
                config.get_value("database.connection_url")
            )

        return cls._engine

    @classmethod
    def run(
        cls,
        *args,
        tx: tp.Optional[sqlalchemy.Connection] = None,
        **kwargs,
    ) -> CursorResult:
        if tx is not None:
            result = tx.execute(*args, **kwargs)
        else:
            engine = cls.get_engine()
            with engine.begin() as tx:
                result = tx.execute(*args, **kwargs)

        return result


def transactional(func):
    def wrapped(
        tx: tp.Optional[sqlalchemy.Connection],
        *args,
        **kwargs,
    ):
        if tx is not None:
            result = func(tx=tx, *args, **kwargs)
        else:
            engine = Repository.get_engine()
            with engine.begin() as tx:
                result = func(tx=tx, *args, **kwargs)

        return result

    return wrapped
