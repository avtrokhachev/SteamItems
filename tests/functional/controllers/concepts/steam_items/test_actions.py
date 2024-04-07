from decimal import Decimal

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


class TestUpdateSteamItem:
    def test_creates_steam_item_when_does_not_exist(self):
        steam_item = db_steam_items.factories.build()

        result = steam_items.update_steam_item(
            link=steam_item.link,
            name=steam_item.name,
            game_id=steam_item.game_id,
            buy_price=steam_item.buy_price,
            sell_price=steam_item.sell_price,
            buy_orders=steam_item.buy_orders,
            sell_orders=steam_item.sell_orders,
            tx=None,
        )

        steam_item.id = result.id
        assert result == steam_item

        db_steam_item = db_steam_items.get_by_link(
            link=steam_item.link,
            tx=None,
        )
        assert db_steam_item == result

    def test_updates_steam_item_when_exists(self):
        steam_item = db_steam_items.factories.create()

        result = steam_items.update_steam_item(
            link=steam_item.link,
            name=steam_item.name,
            game_id=steam_item.game_id,
            buy_price=Decimal("12.34"),
            sell_price=Decimal("23.45"),
            buy_orders=13,
            sell_orders=37,
            tx=None,
        )

        assert result.buy_price == Decimal("12.34")
        assert result.sell_price == Decimal("23.45")
        assert result.buy_orders == 13
        assert result.sell_orders == 37

        result = db_steam_items.get_all(
            tx=None,
        )
        assert len(result) == 1

        result = result[0]
        assert result.buy_price == Decimal("12.34")
        assert result.sell_price == Decimal("23.45")
        assert result.buy_orders == 13
        assert result.sell_orders == 37
