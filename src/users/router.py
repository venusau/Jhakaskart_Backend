from fastapi import APIRouter
from controller import UserController

user_router = APIRouter()


@user_router.get("/users/")
async def get_users():
    return await UserController.get_users()


@user_router.post("/users")
async def create_user(user: dict):
    return await UserController.create_user(user=user)
