from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mydatabase

@app.post("/add_user/")
async def add_user(name: str, age: int):
    user = {"name": name, "age": age}
    await db.users.insert_one(user)
    return {"message": "User added"}

@app.get("/get_users/")
async def get_users():
    return await db.users.find().to_list(10)
