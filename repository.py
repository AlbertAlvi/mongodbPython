from pymongo import MongoClient

client = MongoClient("mongodb:27017")

db = client.dataBase
user = db.user
sectors = db.setores