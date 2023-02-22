from fastapi import FastAPI
from db import init_db, create_client, close_client, get_client
from quizz import quizz_router



app = FastAPI()
app.include_router(quizz_router,
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