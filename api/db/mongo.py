#import os
#from motor.motor_asyncio import AsyncIOMotorClient
#from dotenv import load_dotenv

#load_dotenv()

#MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
#client = AsyncIOMotorClient(MONGO_URL)
#db = client["syntaxia"]

#def get_db():
#    return db

from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client["syntaxia"]

def get_db():
    return db
