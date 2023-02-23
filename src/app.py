from fastapi import FastAPI
from src.db import init_db, create_client, close_client
from src.quizzes import quiz_router

app = FastAPI()
app.include_router(quiz_router,
                   prefix="/quiz",
                   tags=["quizzes"])

@app.on_event("startup")
async def on_startup():
    print("Startup...")
    await create_client()
    await init_db()


@app.on_event("shutdown")
async def on_shutdown():
    print("Shutdown...")
    await close_client()