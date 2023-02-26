from pydantic import BaseModel, Field, validator


class Choice(BaseModel):
    content: str
    is_correct: bool = False


class Question(BaseModel):
    title: str
    content: str
    choices: list[Choice]
    correct_answer: Choice
    grade: int = Field(ge=0, le=100)

    @validator('correct_answer')
    def is_correct_answer_in_choices(cls, v, values, **kwargs):
        if v not in values:
            raise ValueError('the given correct answer is NOT a member of the list of choices')


class Quiz(BaseModel):
    title: str
    questions: list[Question]
    is_login_required: bool = False
