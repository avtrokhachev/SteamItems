import typing as tp
from configparser import SectionProxy

import requests
from MarketItem import MarketItem
from Parser import Parser


class MarketBot:
    def __init__(self, game_id: int, cfg: SectionProxy):
        self.game_id: int = game_id
        self.parser = Parser(game_id)
        self.api_url = cfg["api_url"]

    def update_items(self):
        while True:
            for i in self.parser.get_all_items():
                i = self.parser.get_cost_and_orders(i)
                self.upsert_item(i)

    def upsert_item(self, market_item: MarketItem):
        response = requests.post(self.api_url, json=market_item.get_dict())
