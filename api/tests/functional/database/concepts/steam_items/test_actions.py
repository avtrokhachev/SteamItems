from common.concepts import random
from database.concepts import steam_items


class TestGetAll:
    def test_returns_empty_list_when_no_steam_items(self):
        result = steam_items.get_all(tx=None)

        assert result == []

    def test_correctly_returns_steam_items(self):
        items = [steam_items.factories.create() for _ in range(3)]

        result = steam_items.get_all(tx=None)

        assert result == items


class TestGetById:
    def test_returns_none_when_no_steam_item(self):
        result = steam_items.get_by_id(
            id=random.generate_id(),
            tx=None,
        )

        assert result is None

    def test_ok(self):
        steam_item = steam_items.factories.create()

        result = steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )

        assert result == steam_item


class TestInsert:
    def test_ok(self):
        steam_item = steam_items.factories.build()

        steam_items.insert(
            steam_item=steam_item,
            tx=None,
        )

        result = steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )
        assert result == steam_item


class TestDelete:
    def test_ok(self):
        steam_item = steam_items.factories.create()

        steam_items.delete(
            id=steam_item.id,
            tx=None,
        )

        result = steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )
        assert result is None


class TestUpdate:
    def test_ok(self):
        steam_item = steam_items.factories.create()

        steam_item.sell_orders += 100
        steam_items.update(
            steam_item=steam_item,
            tx=None,
        )

        result = steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )
        assert result.sell_orders == steam_item.sell_orders


class TestUpsert:
    def test_correctly_inserts(self):
        steam_item = steam_items.factories.build()

        steam_items.upsert(
            steam_item=steam_item,
            tx=None,
        )

        result = steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )
        assert result == steam_item

    def test_correctly_updates(self):
        steam_item = steam_items.factories.create()

        steam_item.sell_orders += 100
        steam_items.upsert(
            steam_item=steam_item,
            tx=None,
        )

        result = steam_items.get_by_id(
            id=steam_item.id,
            tx=None,
        )
        assert result.sell_orders == steam_item.sell_orders

        result.sell_orders = steam_item.sell_orders
        assert result == steam_item


class TestGetByLink:
    def test_returns_none_when_no_steam_item(self):
        result = steam_items.get_by_link(
            link=random.generate_string(),
            tx=None,
        )

        assert result is None

    def test_ok(self):
        steam_item = steam_items.factories.create()

        result = steam_items.get_by_link(
            link=steam_item.link,
            tx=None,
        )

        assert result == steam_item
