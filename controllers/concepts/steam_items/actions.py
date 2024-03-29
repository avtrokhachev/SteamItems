from database.concepts import steam_items


def get_steam_item(steam_item_id: str) -> steam_items.SteamItem:
    steam_item = steam_items.get_by_id(id=steam_item_id)

    return steam_item
