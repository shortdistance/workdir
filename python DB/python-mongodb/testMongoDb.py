import pymongo
client = pymongo.MongoClient("localhost", 10000)
db = client.test
print db.name
print db.my_collection
x = db.my_collection_1
print x


db.my_collection.insert_one({"x": 10}).inserted_id
db.my_collection.insert_one({"x": 8}).inserted_id
db.my_collection.insert_one({"x": 11}).inserted_id
db.my_collection.find_one()
for item in db.my_collection.find():
    print(item["x"])

db.my_collection.create_index("x")

for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])

[item["x"] for item in db.my_collection.find().limit(2).skip(1)]
