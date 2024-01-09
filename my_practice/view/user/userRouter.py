from typing import List

from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse

from view.user.schemas import User

user_router = APIRouter(prefix="/user")

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

@user_router.post("/create")
async def create_user(user: List[User]):
    fake_users.extend(user)
    return {
        "status": 200,
        "data": fake_users,
    }
    


@user_router.get("/{user_id}", response_model=List[User])
async def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

# Благодаря этой функции клиент видит ошибки, происходящие на сервере, вместо "Internal server error"
# @user_router.exception_handler(ValidationError)
# async def validation_exception_handler(request: Request, exc: ValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()}),
#     )