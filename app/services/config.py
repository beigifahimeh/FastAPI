import os 

class Config:
    DB_HOST = os.getenv("DB_HOST", "my_database.com")
    DB_USERNAME = os.getenv("DB_USER_NAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
