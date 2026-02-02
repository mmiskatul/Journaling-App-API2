from fastapi import APIRouter, HTTPException
from core.database import db
from core.security import hash_password, verify_password, create_access_token
from models.user import UserCreate
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: UserCreate):
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(400, "Email already exists")

    new_user = {
        "email": user.email,
        "name": user.name,
        "hashed_password": hash_password(user.password),
        "is_premium": False
    }
    res = await db.users.insert_one(new_user)

    token = create_access_token({"sub": str(res.inserted_id)})
    return {"access_token": token}

@router.post("/login")
async def login(email: str, password: str):
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"sub": str(user["_id"])})
    return {"access_token": token}
