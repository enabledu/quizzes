from fastapi import APIRouter

from quizzes.backend.src.quizzes import quiz_router

app = APIRouter(tags=["quizzes"], prefix="/quizzes")

app.include_router(quiz_router, prefix="/quiz", tags=["quizzes"])


@app.get("/")
async def root():
    return {"message": "Hello World from quizzes!"}


