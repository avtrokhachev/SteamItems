import typing as tp

import sqlalchemy

from database.concepts import repository

from .models import SteamItem
from .table import SteamItems


@repository.transactional
def get_all(
    tx: sqlalchemy.Connection,
) -> list[SteamItem]:
    query = sqlalchemy.select(SteamItems)
    result = repository.Repository.run(
        query,
        tx=tx,
    ).fetchall()

    # TODO: fix this, too ugly.
    result = [
        {k: v for k, v in zip(SteamItem.__fields__, raw_steam_item)}
        for raw_steam_item in result
    ]
    result = [SteamItem.model_validate(steam_item) for steam_item in result]
    return result


@repository.transactional
def get_by_id(
    id: str,
    tx: sqlalchemy.Connection,
) -> tp.Optional[SteamItem]:
    query = sqlalchemy.select(SteamItems).filter_by(id=id)
    result = repository.Repository.run(
        query,
        tx=tx,
    ).fetchone()

    if result is not None:
        result = SteamItem.model_validate(
            {k: v for k, v in zip(SteamItem.__fields__, result)}
        )
    return result


@repository.transactional
def get_by_link(
    link: str,
    tx: sqlalchemy.Connection,
) -> tp.Optional[SteamItem]:
    query = sqlalchemy.select(SteamItems).filter_by(link=link)
    result = repository.Repository.run(
        query,
        tx=tx,
    ).fetchone()

    if result is not None:
        result = SteamItem.model_validate(
            {k: v for k, v in zip(SteamItem.__fields__, result)}
        )
    return result


@repository.transactional
def insert(
    steam_item: SteamItem,
    tx: sqlalchemy.Connection,
) -> None:
    query = sqlalchemy.insert(SteamItems).values(steam_item.model_dump())
    repository.Repository.run(
        query,
        tx=tx,
    )


@repository.transactional
def delete(
    id: str,
    tx: sqlalchemy.Connection,
) -> None:
    query = sqlalchemy.delete(SteamItems).filter_by(id=id)
    repository.Repository.run(
        query,
        tx=tx,
    )


@repository.transactional
def update(steam_item: SteamItem, tx: sqlalchemy.Connection) -> None:
    query = sqlalchemy.update(SteamItems).where(SteamItems.id == steam_item.id).values(steam_item.model_dump())
    repository.Repository.run(
        query,
        tx=tx,
    )


@repository.transactional
def upsert(
    steam_item: SteamItem,
    tx: sqlalchemy.Connection,
) -> None:
    existing_steam_item = get_by_id(
        id=steam_item.id,
        tx=tx,
    )
    if existing_steam_item is None:
        insert(
            steam_item=steam_item,
            tx=tx,
        )
    else:
        update(
            steam_item=steam_item,
            tx=tx,
        )
