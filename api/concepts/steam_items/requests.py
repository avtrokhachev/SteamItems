from pydantic import BaseModel


class SteamItemRequest(BaseModel):
    id: str