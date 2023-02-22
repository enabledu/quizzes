import uuid
from typing import Optional

from edgedb import AsyncIOClient
from fastapi import APIRouter, Body, Depends, Query

from db import get_client
from utils import format_query_result, str_to_list

quizz_router = APIRouter()



