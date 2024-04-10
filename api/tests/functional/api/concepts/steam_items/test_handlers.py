import json
from decimal import Decimal

from fastapi.testclient import TestClient

from api.app import app
from common.concepts import random
from database.concepts import steam_items as db_steam_items

client = TestClient(app)


class TestGetSteamItem:
    def test_return_null_when_steam_items_does_not_exist(self):
        response = client.get(f"/steamItems/{random.generate_id()}/get")

        assert response.status_code == 200
        assert response.json() is None

    def test_ok(self):
        steam_item = db_steam_items.factories.create()

        response = client.get(f"/steamItems/{steam_item.id}/get")

        assert response.status_code == 200
        assert response.json() == {
            "id": steam_item.id,
            "link": steam_item.link,
            "name": steam_item.name,
            "game_id": steam_item.game_id,
            "buy_price": str(Decimal(steam_item.buy_price)),
            "sell_price": str(Decimal(steam_item.sell_price)),
            "buy_orders": steam_item.buy_orders,
            "sell_orders": steam_item.sell_orders,
        }


class TestListSteamItems:
    def test_returns_empty_list_when_no_steam_items(self):
        response = client.get("/steamItems/list")

        assert response.status_code == 200
        assert response.json() == []

    def test_ok(self):
        list_of_steam_items = [
            db_steam_items.factories.create() for _ in range(3)
        ]

        response = client.get("/steamItems/list")

        assert response.status_code == 200

        expected_response = [
            {
                "id": steam_item.id,
                "link": steam_item.link,
                "name": steam_item.name,
                "game_id": steam_item.game_id,
                "buy_price": str(Decimal(steam_item.buy_price)),
                "sell_price": str(Decimal(steam_item.sell_price)),
                "buy_orders": steam_item.buy_orders,
                "sell_orders": steam_item.sell_orders,
            }
            for steam_item in list_of_steam_items
        ]
        assert response.json() == expected_response


class TestUpdateSteamItem:
    def test_ok(self):
        steam_item = db_steam_items.factories.create()

        new_steam_item = steam_item.copy()
        new_steam_item.buy_orders += 100

        request = {
            "link": new_steam_item.link,
            "name": new_steam_item.name,
            "game_id": new_steam_item.game_id,
            "buy_price": str(new_steam_item.buy_price),
            "sell_price": str(new_steam_item.sell_price),
            "buy_orders": new_steam_item.buy_orders,
            "sell_orders": new_steam_item.sell_orders,
        }
        response = client.post("/steamItems/update", data=json.dumps(request))

        assert response.status_code == 200
        assert response.json() == {
            "id": steam_item.id,
            "link": steam_item.link,
            "name": steam_item.name,
            "game_id": steam_item.game_id,
            "buy_price": str(Decimal(steam_item.buy_price)),
            "sell_price": str(Decimal(steam_item.sell_price)),
            "buy_orders": steam_item.buy_orders + 100,
            "sell_orders": steam_item.sell_orders,
        }
