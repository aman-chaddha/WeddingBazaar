from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....db.session import get_db
from ....deps import get_current_user
from ....models.user import User
from ....models.vendor import Vendor
from ....schemas.vendor import VendorOut, VendorUpdate

router = APIRouter()


@router.get("/me", response_model=VendorOut)
def get_vendor_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    vendor = db.query(Vendor).filter(Vendor.user_id == current_user.id).first()
    if not vendor:
        # Only auto-create for users with role 'vendor'
        if current_user.role != "vendor":
            raise HTTPException(status_code=404, detail="Vendor profile not found for this user")
        vendor = Vendor(user_id=current_user.id, business_name=current_user.first_name or "")
        db.add(vendor)
        db.commit()
        db.refresh(vendor)
    return vendor


@router.patch("/me", response_model=VendorOut)
def update_vendor_me(
    payload: VendorUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    vendor = db.query(Vendor).filter(Vendor.user_id == current_user.id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor profile not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(vendor, field, value)
    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor
