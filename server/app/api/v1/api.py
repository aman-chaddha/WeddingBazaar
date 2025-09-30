from fastapi import APIRouter

from .endpoints import health, auth
from .endpoints import users, couples

api_router = APIRouter()

# Health
api_router.include_router(health.router, tags=["health"]) 

# Auth (stubs for now)
api_router.include_router(auth.router, prefix="/auth", tags=["auth"]) 

# Users
api_router.include_router(users.router, prefix="/users", tags=["users"]) 

# Couples
api_router.include_router(couples.router, prefix="/couples", tags=["couples"]) 
