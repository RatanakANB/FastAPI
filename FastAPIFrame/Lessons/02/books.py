"""Application entry point for the lesson 02 FastAPI example."""

# ====== Turn in defualt route ===
# from fastapi import Body, FastAPI
# app = FastAPI()

# === Tunr of defual docs route ===
from fastapi import FastAPI

from Routes.bookRoutes import router as book_router
from swaggerReload import setup_swagger_reload

app = FastAPI(docs_url=None)
setup_swagger_reload(app)
app.include_router(book_router)
# =================================