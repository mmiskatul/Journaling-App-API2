from fastapi import APIRouter, Depends, HTTPException
from core.database import db
from core.deps import get_current_user
from datetime import date

router = APIRouter(prefix="/moods", tags=["Moods"])

@router.post("/")
async def set_mood(mood: str, user=Depends(get_current_user)):
    today = str(date.today())
    if await db.moods.find_one({"user_id": user["_id"], "date": today}):
        raise HTTPException(400, "Mood already set")

    await db.moods.insert_one({
        "user_id": user["_id"],
        "mood": mood,
        "date": today
    })
    return {"message": "Mood saved"}
