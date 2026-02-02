from fastapi import FastAPI
from routes import auth, journals, moods, goals

app = FastAPI(title="Journaling Backend")

app.include_router(auth.router)
app.include_router(journals.router)
app.include_router(moods.router)
app.include_router(goals.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
