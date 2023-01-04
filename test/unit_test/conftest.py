import pytest
from app.services.user import UserService

@pytest.fixture
def profile_info():
    profile_info = {
        0:{
        "short_description": "Im 28 years old" ,
        "long_bio": "life is beautiful"
        }
    }
    return profile_info

@pytest.fixture
def user_content():
    content = {
        0:{ 
        "name":"Fahimeh",
        "liked_post":[1] * 9
        },
    }
    return content

@pytest.fixture
def user_service(profile_info, user_content):
    user_service = UserService(profile_info, user_content)
    return user_service