from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read():
    # Для запуска в вебе
    return "uvicorn main:app --reload"


@app.get("/firstname/{firstname}")
def read_name(firstname: str, lastname: str = ""):
    # Для запуска в вебе
    return f"Hello {firstname} {lastname}"


class User(BaseModel):
    name: str
    age: int
    is_admin: bool


@app.put("/user/{user_id}")
def user(user: User):
    return {"name": user.name, "age": user.age, "admin": user.is_admin}


@app.get("/user/{user_id}")
def user(user_id: int):
    return user_id
