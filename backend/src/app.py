from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from quizzes.backend.src.quizzes import quiz_router

app = APIRouter(tags=["quizzes"], prefix="/quizzes")

app.include_router(quiz_router, prefix="/quiz", tags=["quizzes"])


@app.get("/")
async def root():
    return {"message": "Hello World from quizzes!"}


@app.get("/static/default-icon.svg")
async def router_root():
    content = "<img src='/static/default-icon.svg'>"
    return HTMLResponse(content=content)