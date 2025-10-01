from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....db.session import get_db
from ....deps import get_current_user
from ....models.couple import Couple
from ....models.package import Package
from ....models.user import User
from ....schemas.package import PackageCreate, PackageOut

router = APIRouter()


@router.post("/", response_model=PackageOut)
def create_package(
    payload: PackageCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    couple = db.query(Couple).filter(Couple.user_id == current_user.id).first()
    if not couple:
        raise HTTPException(status_code=404, detail="Couple profile not found")

    pkg = Package(couple_id=couple.id, title=payload.title)
    db.add(pkg)
    db.commit()
    db.refresh(pkg)
    return pkg


@router.get("/", response_model=list[PackageOut])
def list_packages(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    couple = db.query(Couple).filter(Couple.user_id == current_user.id).first()
    if not couple:
        raise HTTPException(status_code=404, detail="Couple profile not found")
    pkgs = (
        db.query(Package)
        .filter(Package.couple_id == couple.id)
        .order_by(Package.created_at.desc())
        .all()
    )
    return pkgs
