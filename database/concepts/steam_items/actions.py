import typing as tp

import sqlalchemy

from database.concepts import repository

from .models import SteamItem
from .table import SteamItems


@repository.transactional
def get_all(
    tx=None,
) -> list[SteamItem]:
    query = sqlalchemy.select(SteamItems)
    result = repository.Repository.run(
        query,
        tx=tx,
    )

    result = [SteamItem.model_validate(steam_item) for steam_item in result]
    return result


@repository.transactional
def get_by_id(
    id: str,
    tx=None,
) -> tp.Optional[SteamItem]:
    query = sqlalchemy.select(SteamItems).filter_by(id=id)
    result = repository.Repository.run(
        query,
        tx=tx,
    ).fetchone()

    return result


@repository.transactional
def insert(
    steam_item: SteamItem,
    tx=None,
) -> None:
    query = sqlalchemy.insert(SteamItems).values(steam_item.model_dump())
    repository.Repository.run(
        query,
        tx=tx,
    )


@repository.transactional
def delete(
    id: str,
    tx=None,
) -> None:
    query = sqlalchemy.delete(SteamItems).where(id=id)
    repository.Repository.run(
        query,
        tx=tx,
    )


@repository.transactional
def upsert(
    steam_item: SteamItem,
    tx=None,
):
    existing_steam_item = get_by_id(
        id=steam_item.id,
        tx=tx,
    )
    if existing_steam_item is None:
        delete(
            id=steam_item.id,
            tx=tx,
        )

    insert(
        steam_item=steam_item,
        tx=tx,
    )
