import uuid
from uuid import UUID

from edgedb import AsyncIOClient
from fastapi import (Depends,Form, Body, APIRouter)

from src.db import get_client
from src.models import (Quiz,Question,Choice)

quiz_router =  APIRouter()


@quiz_router.get('/{id}')
async def get_quiz(question_id: uuid.UUID, client: AsyncIOClient = Depends(get_client)) -> Question:
    """get question by id """
    question = await client.query(
        f"""
        select Question {{
            title ,content, choices, grade
        }} filter .id = <uuid>'{question_id}'
    """
    )
    return await client.query_single(question)


@quiz_router.post('/answer')
async def post_answers():
    """Post user's answers to quiz"""
    pass


@quiz_router.get('/correct_answers')
async def get_correct_answers( question_id: uuid.UUID, client: AsyncIOClient = Depends(get_client)):
    """Get the correct answers of a question"""
    question =await client.query_single(
        f"""
             select Question {{
                 choices := (
                     select Choice filter .is_correct = true
             }}filter .id = <uuid>'{question_id}'
            )
        """
    )
    return await client.query_single(question)


@quiz_router.post('/create')
async def create_question(question: Question = Body(),client: AsyncIOClient = Depends(get_client)) -> UUID:
    """create a new question"""
    await client.query_single(
        f"""
            insert Question {{
                title := '{question.title}',
                content := '{question.content}',
                choices := {question.choices},
                grade := '{question.grade}'
            }}     
        """
    )
    return {"msg": f"create question successfully "}