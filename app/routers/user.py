from fastapi import APIRouter
from app.schemas.user import *
from app.services.user import UserService



def create_user_router(profile_info, content) -> APIRouter:
    user_router = APIRouter(prefix= "/user", tags= ["user"])
    user_service = UserService(profile_info, content)
 
    @user_router.get("/all", response_model=multipleUserResponse )
    def get_all_users_paginated(start: int = 0,limit: int = 2):
        users = user_service.get_all_users_pagination(start= start, limit= limit)
        formatted_users = multipleUserResponse(users= users)
        return formatted_users

    @user_router.get("/{user_id}", response_model= FullUserProfile)
    def get_user_by_id(user_id: int):
        full_user_profile = user_service.get_user_info(user_id)
        return full_user_profile

    @user_router.post("/", response_model= createUserResponse)
    def add_user(full_profile_info: FullUserProfile):
        return createUserResponse(user_id = user_service.create_update_user(full_profile_info))

    @user_router.put("/{user_id}")
    def update_user(user_id: int, full_Profile_info: FullUserProfile):
        user_service.create_update_user(full_Profile_info, user_id)
        return None

    @user_router.delete("/{user_id}")
    def remove_user(user_id: int):
        user_service.delete_user(user_id)
        return None
    return user_router