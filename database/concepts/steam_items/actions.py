import typing as tp

import sqlalchemy

from database.concepts import repository

from .models import SteamItem
from .table import SteamItems


def get_all() -> list[SteamItem]:
    query = sqlalchemy.select(SteamItems)
    result = repository.Repository.run(query)

    result = [SteamItem.model_validate(steam_item) for steam_item in result]
    return result


def get_by_id(id: str) -> tp.Optional[SteamItem]:
    query = sqlalchemy.select(SteamItems).filter_by(id=id)
    result = repository.Repository.run(query).fetchone()

    return result


def insert(steam_item: SteamItem) -> None:
    query = sqlalchemy.insert(SteamItems).values(steam_item.model_dump())
    repository.Repository.run(query)


def delete(id: str) -> None:
    query = sqlalchemy.delete(SteamItems).where(id=id)
    repository.Repository.run(query)


def upsert(steam_item: SteamItem):
    existing_steam_item = get_by_id(id=steam_item.id)
    if existing_steam_item is None:
        delete(id=steam_item.id)

    insert(steam_item=steam_item)
