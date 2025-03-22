from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient

class Settings(BaseSettings):
    MONGO_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client["mydatabase"]
collection = db["users"]

class User(BaseModel):
    name: str
    age: int

@app.post("/add_user/")
async def add_user(user: User):
    new_user = await collection.insert_one(user.model_dump())
    return {"message": "User added", "user_id": str(new_user.inserted_id)}

@app.get("/get_users/")
async def get_users():
    users = await collection.find().to_list(100)
    return users

# uvicorn mdb3:app --reload