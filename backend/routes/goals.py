from fastapi import APIRouter, Depends
from core.database import db
from core.deps import get_current_user
from datetime import datetime

router = APIRouter(prefix="/goals", tags=["Goals"])

@router.post("/")
async def create_goal(title: str, user=Depends(get_current_user)):
    await db.goals.insert_one({
        "user_id": user["_id"],
        "title": title,
        "status": "ongoing",
        "created_at": datetime.utcnow()
    })
    return {"message": "Goal created"}
