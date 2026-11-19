from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.core.config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

