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
