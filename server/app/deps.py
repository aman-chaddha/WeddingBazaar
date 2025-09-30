from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from uuid import UUID

from .core.security import decode_token
from .db.session import get_db
from .crud.user import get_user_by_email
from .models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user_id_or_email = payload["sub"]
    # Our token uses user.id as subject; we can look up by id
    # But we only have get_user_by_email; implement quick id getter here
    try:
        uid = UUID(user_id_or_email)
    except Exception:
        # fallback to email
        user = get_user_by_email(db, user_id_or_email)
    else:
        user = db.query(User).filter(User.id == uid).first()

    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive or not found user")
    return user
