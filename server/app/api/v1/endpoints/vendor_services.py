from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....db.session import get_db
from ....deps import get_current_user
from ....models.user import User
from ....models.vendor import Vendor
from ....models.vendor_service import VendorService
from ....schemas.vendor_service import VendorServiceCreate, VendorServiceOut

router = APIRouter()


@router.post("/", response_model=VendorServiceOut)
def create_vendor_service(
    payload: VendorServiceCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    vendor = db.query(Vendor).filter(Vendor.user_id == current_user.id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor profile not found")

    svc = VendorService(
        vendor_id=vendor.id,
        category=payload.category,
        title=payload.title,
        base_price=payload.base_price,
        min_price=payload.min_price,
        max_price=payload.max_price,
        pricing_unit=payload.pricing_unit,
        details=payload.details,
    )
    db.add(svc)
    db.commit()
    db.refresh(svc)
    return svc


@router.get("/", response_model=list[VendorServiceOut])
def list_my_vendor_services(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    vendor = db.query(Vendor).filter(Vendor.user_id == current_user.id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor profile not found")
    services = db.query(VendorService).filter(VendorService.vendor_id == vendor.id).all()
    return services
