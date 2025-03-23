from fastapi import FastAPI
from repository import UserRepository
from models import User, UserInDB
from fastapi import HTTPException
from typing import List

app = FastAPI()

@app.post("/users/", response_model=str)
def create_user(user: User):
    return UserRepository.create_user(user)

@app.get("/users/", response_model=List[UserInDB])
def get_users():
    return UserRepository.get_users()

@app.get("/users/{user_id}", response_model=UserInDB)
def get_user(user_id: str):
    return UserRepository.get_user(user_id)

@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    UserRepository.update_user(user_id, user)
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    UserRepository.delete_user(user_id)
    return {"message": "User deleted successfully"}
