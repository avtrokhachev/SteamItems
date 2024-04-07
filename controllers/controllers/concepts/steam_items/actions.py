from database.concepts import repository, steam_items


@repository.transactional
def list_steam_items(
    tx: repository.Connection,
) -> list[steam_items.SteamItem]:
    list_steam_items = steam_items.get_all(
        tx=tx,
    )

    return list_steam_items


@repository.transactional
def get_steam_item(
    steam_item_id: str,
    tx: repository.Connection,
) -> steam_items.SteamItem:
    steam_item = steam_items.get_by_id(
        id=steam_item_id,
        tx=tx,
    )

    return steam_item


@repository.transactional
def create_steam_item(
    steam_item: steam_items.SteamItem,
    tx: repository.Connection,
) -> steam_items.SteamItem:
    steam_items.insert(
        steam_item=steam_item,
        tx=tx,
    )

    return steam_item
