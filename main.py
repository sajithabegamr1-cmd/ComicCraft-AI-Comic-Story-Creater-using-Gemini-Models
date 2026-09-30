from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router

app = FastAPI(title="ComicCraft - AI Comic")

app.include_router(router)