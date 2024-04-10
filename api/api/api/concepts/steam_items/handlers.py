from typing import Optional

from fastapi import APIRouter

from controllers.concepts import steam_items

from .requests import UpdateSteamItemRequest
from .responses import SteamItemResponse

router = APIRouter(
    prefix="/steamItems",
)


# TODO: add 404 status_code on not found
@router.get(
    path="/{steam_item_id}/get",
    response_model=Optional[SteamItemResponse],
)
def get_steam_item(steam_item_id: str) -> Optional[SteamItemResponse]:
    steam_item = steam_items.get_steam_item(
        steam_item_id=steam_item_id,
        tx=None,
    )

    response = None
    if steam_item:
        response = SteamItemResponse.model_validate(
            steam_item.model_dump(mode="json")
        )
    return response


@router.get(
    path="/list",
    response_model=list[SteamItemResponse],
)
def list_steam_items() -> list[SteamItemResponse]:
    list_of_steam_items = steam_items.list_steam_items(
        tx=None,
    )

    list_of_steam_items = [
        SteamItemResponse.model_validate(steam_item.model_dump(mode="json"))
        for steam_item in list_of_steam_items
    ]
    return list_of_steam_items


@router.post(
    path="/update",
    response_model=SteamItemResponse,
)
def update_steam_item(request: UpdateSteamItemRequest) -> SteamItemResponse:
    steam_item = steam_items.update_steam_item(
        link=request.link,
        name=request.name,
        game_id=request.game_id,
        buy_price=request.buy_price,
        sell_price=request.sell_price,
        buy_orders=request.buy_orders,
        sell_orders=request.sell_orders,
        tx=None,
    )

    response = SteamItemResponse.model_validate(
        steam_item.model_dump(mode="json")
    )
    return response
