from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import get_db
from models import User, UserProfile
from schemas import UserCreate, UserResponse, UserLogin, Token
from utils.security import get_password_hash, verify_password, create_access_token

# Authentication Routes
auth_router = APIRouter()


@auth_router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email already exists
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )

    # Hash the user password and save to DB
    hashed_pass = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pass
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Automatically create a default empty profile for the new user
    db_profile = UserProfile(
        user_id=db_user.id,
        full_name=user.username,
        bio="",
        interests=""
    )
    db.add(db_profile)
    db.commit()

    return db_user


@auth_router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )

    # Generate JWT access token
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
