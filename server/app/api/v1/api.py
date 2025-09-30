from fastapi import APIRouter

from .endpoints import health, auth

api_router = APIRouter()

# Health
api_router.include_router(health.router, tags=["health"]) 

# Auth (stubs for now)
api_router.include_router(auth.router, prefix="/auth", tags=["auth"]) 
