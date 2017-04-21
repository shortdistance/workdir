#-*-coding:utf-8 -*-

import pymongo

import random


client = pymongo.MongoClient("localhost", 27017)
db = client.test
print db.name

print db.my_collection

print  db.my_collection.insert_one({"x": 10}).inserted_id

print db.my_collection.insert_one({"x": 8}).inserted_id

print db.my_collection.insert_one({"x": 11}).inserted_id

db.my_collection.find_one()

for item in db.my_collection.find():
    print item["x"]

db.my_collection.create_index("x")

for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print item["x"]

print [item["x"] for item in db.my_collection.find().limit(2).skip(1)]

db1 = client.svn
print db1.name
db1.my_collection.insert_one({"repos":"qmd", "repos_url":"http://172.16.9.106:9001/svn/qmd"})
print db1.my_collection.find_one()
for item in db1.my_collection.find().sort("repos", pymongo.ASCENDING):
    print item["repos"]