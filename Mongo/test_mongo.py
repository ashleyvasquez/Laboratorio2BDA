from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
collection.insert_one({"name": "test"})
print(list(collection.find()))