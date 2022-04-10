import datetime
import os
from random import randint

from pymongo import MongoClient

# Connect to DB
client = MongoClient("mongodb://sa:password@localhost:27017/")

# clear db, if already exists
client.drop_database("mydb")

mydb = client.mydb
print(client.list_database_names())

print("-" * 25)

# Sample random data
names = ["Audi","BMW","Jaguar","Tata","Ford","Tesla","Toyota"]
type = ["Ltd","Inc","Company","Corp"]
model = ["Roadster","X2","Q5","Altise","Camry","Nano","Mastang"]

# Generate and insert random data
for n in range(1,50):
    data = {
        "name": names[randint(0,(len(names)-1))] + " " + type[randint(0,(len(type)-1))],
        "rating": randint(1,5),
        "model": model[randint(0,(len(type)-1))]
    }

    #Insert data
    result = mydb.reviews.insert_one(data)
    print(f"Created: {n} => {result.inserted_id}")

print("-" * 25)

print(client.list_database_names())
print("Insert Done")

print("-" * 25)

# Get 5-star reviews
fiveStar = mydb.reviews.find_one({"rating": 5})
print(fiveStar)

print("-" * 25)

# Get 5-star reviews count
fiveStarCount = mydb.reviews.count_documents({"rating": 5})
print(fiveStarCount)

print("-" * 25)