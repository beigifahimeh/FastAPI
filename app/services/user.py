from ..schemas.user import FullUserProfile, User
from ..exceptions import UserNotFound


class UserService: 
    def __init__(self, profile_info: dict, content: dict):
        self.profile_info = profile_info
        self.content = content

    def get_all_users_pagination(self,start: int, limit: int) -> list[FullUserProfile]:
        listOfUser = []
        keys = list(self.profile_info.keys())
        for index in range(start, len(keys)):
            if index < start:
                continue
            current_key = self.get_user_info(index)
            listOfUser.append(current_key)
            if len(listOfUser)>= limit:
                break
        return listOfUser

    def get_user_info(self, user_id: int  = 0) -> FullUserProfile:    
        profileInfo = self.profile_info[user_id]
        user_content = self.content[user_id]

        user = User(**user_content)
        full_user_profile = {**profileInfo, **user.dict()}
        return FullUserProfile(**full_user_profile)
    
    def create_update_user(self, full_profile_info: FullUserProfile, new_user_id: int = None) -> int:
        if new_user_id is None:
            new_user_id = len(self.profile_info)
        short_description = full_profile_info.short_description
        long_bio = full_profile_info.long_bio
        liked_posts = full_profile_info.liked_post
        self.content[new_user_id] =  {"liked_post": liked_posts}
        self.profile_info[new_user_id] = {
            "short_description": short_description,
            "long_bio": long_bio
        }
        return new_user_id

    def delete_user(self, user_id: int)-> None:
        if user_id not in self.profile_info:
            raise UserNotFound 
        del self.profile_info[user_id]
        del self.content[user_id]

    