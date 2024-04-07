from decimal import Decimal

from pydantic import BaseModel


class SteamItem(BaseModel):
    id: str
    link: str
    name: str
    game_id: int
    buy_price: Decimal
    sell_price: Decimal
    buy_orders: int
    sell_orders: int
