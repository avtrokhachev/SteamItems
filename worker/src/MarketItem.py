from __future__ import annotations

import dataclasses
import json
import typing as tp
from dataclasses import dataclass
from decimal import Decimal

import bs4


@dataclass
class MarketItem:
    link: str
    name: str
    game_id: int
    buy_price: tp.Optional[Decimal] = None
    sell_price: tp.Optional[Decimal] = None
    buy_orders: tp.Optional[int] = None
    sell_orders: tp.Optional[int] = None

    @classmethod
    def from_raw_html(
        cls, raw_html: bs4.element.PageElement, game_id: int
    ) -> MarketItem:
        item_link = raw_html["href"]
        context = raw_html.find_next(
            "div", {"class": "market_listing_item_name_block"}
        )
        item_name = context.find_next(
            "span", {"class": "market_listing_item_name"}
        ).text
        return cls(item_link, item_name, game_id)

    @classmethod
    def from_tuple(cls, data: tuple) -> MarketItem:
        return cls(
            data[0],
            data[1],
            data[2],
            Decimal(data[3]),
            Decimal(data[4]),
            data[5],
            data[6],
        )

    def get_dict(self) -> dict:
        ans = dataclasses.asdict(self)
        ans["buy_price"] = str(ans["buy_price"])
        ans["sell_price"] = str(ans["sell_price"])
        return ans

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
