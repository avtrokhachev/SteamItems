from decimal import Decimal

from pydantic import BaseModel, condecimal


class SteamItem(BaseModel):
    id: str
    link: str
    name: str
    game_id: int
    buy_price: condecimal(decimal_places=2)
    sell_price: condecimal(decimal_places=2)
    buy_orders: int
    sell_orders: int
