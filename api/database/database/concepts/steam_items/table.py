from sqlalchemy import DECIMAL, Column, Integer, String

from database.concepts import repository


class SteamItems(repository.Base):
    __tablename__ = "steam_items"

    id = Column(String, primary_key=True, nullable=False)
    link = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    game_id = Column(Integer, nullable=False)
    buy_price = Column(DECIMAL, nullable=False)
    sell_price = Column(DECIMAL, nullable=False)
    buy_orders = Column(Integer, nullable=False)
    sell_orders = Column(Integer, nullable=False)
