from pymongo import MongoClient
from bson import ObjectId
from fastapi import HTTPException
from models import User, UserInDB
from typing import List
from config import settings


client = MongoClient(settings.MONGO_URI)
db = client[settings.DB_NAME]
collection = db[settings.COLLECTION_NAME]


class UserRepository:
    @staticmethod
    def create_user(user: User) -> str:
        result = collection.insert_one(user.model_dump())
        return str(result.inserted_id)

    @staticmethod
    def get_users() -> List[UserInDB]:
        users = collection.find()
        return [UserInDB(id=str(user["_id"]), **user) for user in users]

    @staticmethod
    def get_user(user_id: str) -> UserInDB:
        user = collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserInDB(id=str(user["_id"]), **user)

    @staticmethod
    def update_user(user_id: str, user: User):
        result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.model_dump()})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="User not found or no change detected")

    @staticmethod
    def delete_user(user_id: str):
        result = collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
