from uuid import UUID

from fastapi import (FastAPI,
                     Depends,
                     Form, Body)
from quizzes.models import (Quiz,
                            Question,
                            Choice)

app = FastAPI()


@app.get('/quiz/{id}')
async def get_quiz(id: UUID) -> Quiz:
    pass


@app.post('/answer')
async def post_answers():
    """Post user's answers to quiz"""
    pass


@app.get('/correct_answers')
async def get_correct_answers():
    """Get the correct answers of a quiz"""
    pass


@app.post('/create')
async def create_quiz(quiz: Quiz = Body()) -> UUID:
    """create a new quiz"""

