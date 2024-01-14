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


def get_by_link(link: str) -> tp.Optional[SteamItem]:
    query = sqlalchemy.select(SteamItems).where(link=link)
    result = repository.Repository.run(query).fetchone()

    return result


def insert(steam_item: SteamItem) -> None:
    query = sqlalchemy.insert(SteamItem).values(steam_item.model_dump())
    repository.Repository.run(query)


def delete(link: str) -> None:
    query = sqlalchemy.delete(SteamItems).where(link=link)
    repository.Repository.run(query)


def upsert(steam_item: SteamItem):
    existing_steam_item = get_by_link(link=steam_item.link)
    if existing_steam_item:
        delete(link=steam_item.link)

    insert(steam_item=steam_item)
