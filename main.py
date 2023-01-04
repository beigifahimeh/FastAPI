from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handler import add_exception_handlers


def create_profile_info_user_content():
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
    return profile_info, content

def  create_application() -> FastAPI:
    profile_info, user_content = create_profile_info_user_content()
    user_router = create_user_router(profile_info, user_content )
    
    app = FastAPI()
    app.include_router(user_router)
    add_exception_handlers(app)

    return app





app = create_application()