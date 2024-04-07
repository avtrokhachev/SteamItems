from fastapi.testclient import TestClient

from api.app import app
from common.concepts import random
from database.concepts import steam_items as db_steam_items

client = TestClient(app)


class TestGetSteamItem:
    def test_return_null_when_steam_items_does_not_exist(self):
        response = client.get(f"/steamItems/{random.generate_id()}/get")

        assert response.status_code == 404
        assert response.json() == {
            "detail": "Not Found",
        }

    def test_ok(self):
        steam_item = db_steam_items.factories.create()

        response = client.get(f"/steamItems/{steam_item.id}/get")

        assert response.status_code == 200
        print(response.json())
