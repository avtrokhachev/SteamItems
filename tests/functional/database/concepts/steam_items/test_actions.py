from database.concepts import steam_items


class TestGetAll:
    def test_returns_empty_list_when_no_steam_items(self):
        result = steam_items.get_all()

        assert result == []

    def test_correctly_returns_steam_items(self):
        pass
