from pydantic import BaseModel

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