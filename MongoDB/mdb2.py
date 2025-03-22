import os
from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["mydatabase"]
collection = db["users"]

class User(BaseModel):
    name: str
    age: int

@app.post("/add_user/")
async def add_user(user: User):
    new_user = await collection.insert_one(user.model_dump())  # Use model_dump()0
    return {"message": "User added", "user_id": str(new_user.inserted_id)}

@app.get("/get_users/")
async def get_users():
    users = await collection.find().to_list(100)
    return users


# uvicorn mdb2:app --reload





