from controllers.concepts import steam_items
from database.concepts import steam_items as db_steam_items


class TestGetSteamItem:
    def test_ok(self):
        steam_item = db_steam_items.factories.create()

        result = steam_items.get_steam_item(
            steam_item_id=steam_item.id,
            tx=None,
        )

        assert result == steam_item


class TestListSteamItems:
    def test_returns_empty_list_when_no_steam_items(self):
        result = steam_items.list_steam_items(
            tx=None,
        )

        assert result == []

    def test_ok(self):
        list_of_steam_items = [
            db_steam_items.factories.create() for _ in range(3)
        ]

        result = steam_items.list_steam_items(
            tx=None,
        )

        assert result == list_of_steam_items


class TestCreateSteamItem:
    def test_ok(self):
        steam_item = db_steam_items.factories.build()

        result = steam_items.create_steam_item(
            steam_item=steam_item,
            tx=None,
        )

        assert result == steam_item

        result = db_steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )
        assert result == steam_item
