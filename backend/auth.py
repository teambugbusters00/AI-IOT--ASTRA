from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from models import UserSignup, UserLogin
from database import users_db
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

@router.post("/signup")
def signup(user: UserSignup):
    logger.info(f"Backend signup attempt for email: {user.email}")
    if user.email in users_db:
        logger.warning(f"Backend signup failed - user already exists: {user.email}")
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[user.email] = {
        "name": user.name,
        "password": hash_password(user.password)
    }
    logger.info(f"Backend signup successful for: {user.email}")
    return {"message": "Account created successfully"}

@router.post("/login")
def login(user: UserLogin):
    logger.info(f"Backend login attempt for email: {user.email}")
    db_user = users_db.get(user.email)
    if not db_user or not verify_password(user.password, db_user["password"]):
        logger.warning(f"Backend login failed - invalid credentials: {user.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    logger.info(f"Backend login successful for: {user.email}")
    return {
        "message": "Login successful",
        "user": db_user["name"]
    }
