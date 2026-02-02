from pydantic import BaseModel

class JournalCreate(BaseModel):
    title: str
    content: str
