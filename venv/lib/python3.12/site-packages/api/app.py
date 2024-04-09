from fastapi import FastAPI

from api.concepts.steam_items.handlers import router

app = FastAPI()
app.include_router(router)
