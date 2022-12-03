from fastapi import FastAPI

from pydantic import BaseModel, Field

app = FastAPI()
profile_info = {
        0:{
        "short_description": "Im 28 years old" ,
        "long_bio": "life is beautiful"
        }
    }
content = {
        0:{ 
        "name":"Fahimeh",
        "liked_post":[1] * 9
        },
}

class User(BaseModel):
    name: str | None
    liked_post: list[int]| None

class FullUserProfile(User):
    short_description : str
    long_bio: str

class createUserResponse(BaseModel):
    user_id : int

class multipleUserResponse(BaseModel):
    users:list[FullUserProfile]

def create_update_user(full_profile_info: FullUserProfile, new_user_id: int = None) -> int:
    if new_user_id is None:
        new_user_id = len(profile_info)
    short_description = full_profile_info.short_description
    long_bio = full_profile_info.long_bio
    liked_posts = full_profile_info.liked_post
    content[new_user_id] =  {"liked_post": liked_posts}
    profile_info[new_user_id] = {
        "short_description": short_description,
        "long_bio": long_bio
    }
    return new_user_id

def delete_user(user_id: int)-> None:
    del profile_info[user_id]
    del content[user_id]



def get_all_users_pagination(start: int, limit: int) -> list[FullUserProfile]:
    listOfUser = []
    keys = list(profile_info.keys())
    for index in range(start, len(keys)):
        if index < start:
            continue
        current_key = get_user_info(index)
        listOfUser.append(current_key)
        if len(listOfUser)>= limit:
            break
    return listOfUser


def get_user_info(user_id: int  = 0) -> FullUserProfile:
    profileInfo = profile_info[user_id]
    user_content = content[user_id]
    user = User(**user_content)
    full_user_profile = {**profileInfo, **user.dict()}
    return FullUserProfile(**full_user_profile)

@app.get("/user/me", response_model= FullUserProfile)
def test_endpoint():
    full_user_profile = get_user_info()
    return full_user_profile

@app.get("/user/{user_id}", response_model= FullUserProfile)
def get_user_by_id(user_id: int):
    full_user_profile = get_user_info(user_id)
    return full_user_profile
@app.post("/users", response_model= createUserResponse)
def add_user(full_profile_info: FullUserProfile):
    return createUserResponse(user_id =  create_update_user(full_profile_info))


@app.get("/users", response_model=multipleUserResponse )
def get_all_users_paginated(start: int = 0,limit: int = 2):
    users = get_all_users_pagination(start= start, limit= limit)
    formatted_users = multipleUserResponse(users= users)
    return formatted_users

@app.put("/user/{user_id}")
def update_user(user_id: int, full_Profile_info: FullUserProfile):
    create_update_user(full_Profile_info, user_id)
    return None

@app.delete("/user/{user_id}")
def remove_user(user_id: int):
    delete_user(user_id)
    return None
