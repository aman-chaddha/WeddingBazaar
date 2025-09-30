from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from ....deps import get_current_user
from ....db.session import get_db
from ....schemas.couple import CoupleOut, CoupleUpdate
from ....models.user import User
from ....models.couple import Couple

router = APIRouter()


@router.get("/me", response_model=CoupleOut)
def get_couple_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    couple = db.query(Couple).filter(Couple.user_id == current_user.id).first()
    if not couple:
        # lazily create couple profile on first access
        couple = Couple(user_id=current_user.id)
        db.add(couple)
        db.commit()
        db.refresh(couple)
    return couple


@router.patch("/me", response_model=CoupleOut)
def update_couple_me(
    payload: CoupleUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    couple = db.query(Couple).filter(Couple.user_id == current_user.id).first()
    if not couple:
        raise HTTPException(status_code=404, detail="Couple profile not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(couple, field, value)
    db.add(couple)
    db.commit()
    db.refresh(couple)
    return couple
