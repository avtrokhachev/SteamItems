from typing import Optional

from fastapi import APIRouter

from controllers.concepts import steam_items

from .requests import SteamItemRequest
from .responses import SteamItemResponse

router = APIRouter(
    prefix="/steamItems",
)


@router.get(
    path="/get/{steam_item_id}",
    response_model=Optional[SteamItemResponse],
)
def get_all(steam_item_id: str) -> Optional[SteamItemResponse]:
    steam_item = steam_items.get_steam_item(
        steam_item_id=steam_item_id,
        tx=None,
    )

    response = None
    if steam_item:
        response = SteamItemResponse(steam_item.model_dump(mode="json"))
    return response
