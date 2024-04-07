from decimal import Decimal

from common.concepts import random
from database.concepts import repository, steam_items


@repository.transactional
def list_steam_items(
    tx: repository.Connection,
) -> list[steam_items.SteamItem]:
    list_of_steam_items = steam_items.get_all(
        tx=tx,
    )

    return list_of_steam_items


@repository.transactional
def get_steam_item(
    steam_item_id: str,
    tx: repository.Connection,
) -> steam_items.SteamItem:
    steam_item = steam_items.get_by_id(
        id=steam_item_id,
        tx=tx,
    )

    return steam_item


@repository.transactional
def update_steam_item(
    link: str,
    name: str,
    game_id: int,
    buy_price: Decimal,
    sell_price: Decimal,
    buy_orders: int,
    sell_orders: int,
    tx: repository.Connection,
) -> steam_items.SteamItem:
    steam_item = steam_items.get_by_link(
        link=link,
        tx=tx,
    )
    if steam_item is not None:
        steam_item.buy_price = buy_price
        steam_item.sell_price = sell_price
        steam_item.buy_orders = buy_orders
        steam_item.sell_orders = sell_orders
    else:
        steam_item = steam_items.SteamItem.model_validate(
            {
                "id": random.generate_id(),
                "link": link,
                "name": name,
                "game_id": game_id,
                "buy_price": buy_price,
                "sell_price": sell_price,
                "buy_orders": buy_orders,
                "sell_orders": sell_orders,
            },
        )

    steam_items.upsert(
        steam_item=steam_item,
        tx=tx,
    )

    return steam_item
