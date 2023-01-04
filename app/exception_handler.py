from app.exceptions import UserNotFound
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFound)
    def handle_user_not_found(req:Request, ex: UserNotFound):
        return JSONResponse(content="user doesnt exits", status_code=404)
    

    return None