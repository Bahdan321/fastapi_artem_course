from fastapi import APIRouter
from view.operations.operationsRouter import operations_router
from view.user.userRouter import user_router

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(operations_router)
main_api_router.include_router(user_router)

