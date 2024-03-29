from pydantic import BaseModel
from decimal import Decimal


class SteamItemResponse(BaseModel):
    link: str
    name: str
    game_id: int
    buy_price: Decimal
    sell_price: Decimal
    buy_orders: int
    sell_orders: int