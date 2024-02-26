from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import urls, db

version = 1

app = FastAPI(
    title="ETHICS GLOBAL",
    description="API encripting and desencripting text",
    version=f"v{version}",
    redoc_url=f"/api/v{version}/redoc",
    docs_url=f"/api/v{version}/docs"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    urls.urls
)

app.add_event_handler(
    "startup",
    db.connect_db
)
