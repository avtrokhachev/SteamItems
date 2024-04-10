from decimal import Decimal
from typing import Optional

from common.concepts import random

from .actions import insert
from .models import SteamItem


def build(
    id: Optional[str] = None,
    link: Optional[str] = None,
    name: Optional[str] = None,
    game_id: int = 100,
    buy_price: Optional[Decimal] = None,
    sell_price: Optional[Decimal] = None,
    buy_orders: Optional[int] = None,
    sell_orders: Optional[int] = None,
) -> SteamItem:
    steam_item = SteamItem(
        id=id or random.generate_id(),
        link=link or random.generate_string(),
        name=name or random.generate_string(),
        game_id=game_id,
        buy_price=buy_price or random.generate_decimal(),
        sell_price=sell_price or random.generate_decimal(),
        buy_orders=buy_orders or random.generate_int(),
        sell_orders=sell_orders or random.generate_int(),
    )

    return steam_item


def create(
    id: Optional[str] = None,
    link: Optional[str] = None,
    name: Optional[str] = None,
    game_id: int = 100,
    buy_price: Optional[Decimal] = None,
    sell_price: Optional[Decimal] = None,
    buy_orders: Optional[int] = None,
    sell_orders: Optional[int] = None,
) -> SteamItem:
    steam_item = build(
        id=id,
        link=link,
        name=name,
        game_id=game_id,
        buy_price=buy_price,
        sell_price=sell_price,
        buy_orders=buy_orders,
        sell_orders=sell_orders,
    )
    insert(
        steam_item=steam_item,
        tx=None,
    )

    return steam_item
