from fastapi import APIRouter

from .endpoints import auth, couples, health, packages, users, vendor_services, vendors

api_router = APIRouter()

# Health
api_router.include_router(health.router, tags=["health"]) 

# Auth (stubs for now)
api_router.include_router(auth.router, prefix="/auth", tags=["auth"]) 

# Users
api_router.include_router(users.router, prefix="/users", tags=["users"]) 

# Couples
api_router.include_router(couples.router, prefix="/couples", tags=["couples"]) 

# Vendors & Services
api_router.include_router(vendors.router, prefix="/vendors", tags=["vendors"]) 
api_router.include_router(
    vendor_services.router,
    prefix="/vendor-services",
    tags=["vendor-services"],
) 

# Packages
api_router.include_router(packages.router, prefix="/packages", tags=["packages"]) 
