import logging
import sys
import typing as tp
from configparser import SectionProxy

import requests
from MarketItem import MarketItem
from Parser import Parser

log = logging.getLogger(__name__)
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.INFO)


class MarketBot:
    def __init__(self, game_id: int, cfg: SectionProxy):
        self.game_id: int = game_id
        self.parser = Parser(game_id)
        self.api_url = cfg["api_url"]

    def start(self):
        log.info(
            f"MarketBot start working for game_id={self.game_id}, api_url={self.api_url}"
        )
        for item in self.parser.iterate_over_items():
            self.upsert_item(item)

    def upsert_item(self, market_item: MarketItem):
        try:
            response = requests.post(self.api_url, json=market_item.get_dict())
        except Exception as exc:
            log.error(
                f"Error occurred while trying to post handler to update steam_item link={market_item.link}, e={exc}"
            )
            return

        if response.status_code == 200:
            log.info(
                f"Successfully updated steam_item link={market_item.link}, code={response.status_code}"
            )
        else:
            log.error(
                f"Error occurred on steam_item update link={market_item.link}, code={response.status_code}"
            )
