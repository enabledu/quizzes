import uuid
from uuid import UUID

from edgedb import AsyncIOClient
from fastapi import (Depends,Form, Body, APIRouter)

from enabled.backend.src.database import get_client
from quizzes.backend.src.models import (Quiz,Question,Choice)

quiz_router = APIRouter()


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
async def create_question(question: Question  = Body(),client: AsyncIOClient = Depends(get_client)):
    """create a new question"""
    booleans = {"False": "false", "True": "true"}
    print(question.choices)
    first_choice = question.choices.pop(0)

    question_id = await client.query_single(f"""
        select(
        insert Question {{
            title := <str>'{question.title}',
            content := <str>'{question.content}',
            grade := <int16>'{question.grade}',
            choices :=(
                insert Choice {{
                        content := <str>'{first_choice.content}' ,
                        is_correct := <bool>{booleans[str(first_choice.is_correct)]}
                    }}
                ),
        }}
        ){{id}}
    """)
    print("????????", question_id, dir(question_id))
    for choice in question.choices:
        create_question_query= f"""
        update Question filter .id = <uuid>'{question_id.id}' set {{
                title := .title,
                content := .content,
                grade :=.grade,
                choices +=(
                    insert Choice {{
                            content := <str>'{choice.content}' ,
                            is_correct := <bool>{booleans[str(choice.is_correct)]}
                        }}
                    )
            }} 
        """
        print(create_question_query)
        await client.query_single(create_question_query)

    return {"msg": f"  Created question with id : {question_id}  "}
