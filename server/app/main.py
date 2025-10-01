from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.v1.api import api_router
from .core.config import settings
from .db import base as model_base
from .db.session import engine

app = FastAPI(
    title="WeddingBazaar API",
    version="0.1.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(api_router, prefix="/api/v1")


@app.get("/api/health", tags=["health"])  # convenience root health
async def root_health():
    return {"status": "ok"}


@app.on_event("startup")
def on_startup():
    # Dev convenience: create tables automatically
    if settings.AUTO_CREATE_TABLES:
        try:
            model_base.Base.metadata.create_all(bind=engine)
        except Exception as e:
            # Avoid crashing app if DB is not ready; log to console
            print(f"[startup] Skipped creating tables (DB not ready?): {e}")
