from fastapi import FastAPI
from concepts.steam_items.handlers import router

app = FastAPI()
app.include_router(router, prefix="/auth")