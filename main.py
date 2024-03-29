from api.concepts.steam_items.handlers import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router, prefix="/auth")
