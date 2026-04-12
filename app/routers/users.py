from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from passlib.context import CryptContext
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
import bcrypt

router = APIRouter(prefix="/users", tags=["Users"])

# Password hashing setup
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_pwd = hash_password(user.password)

    # Create new user
    db_user = User(
        email=user.email, username=user.username, hashed_password=hashed_pwd
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
