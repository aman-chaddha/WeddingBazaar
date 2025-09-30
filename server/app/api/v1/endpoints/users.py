from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ....deps import get_current_user
from ....db.session import get_db
from ....schemas.user import UserOut
from ....models.user import User

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return current_user
