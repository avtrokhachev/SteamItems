from database.concepts import repository, steam_items


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
