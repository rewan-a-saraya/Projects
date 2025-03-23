from pymongo import MongoClient
from config import settings


client = MongoClient(settings.MONGO_URI)
db = client[settings.DB_NAME]
collection = db[settings.COLLECTION_NAME]
