from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['products']

product_one = {"name": "teclado"}
product_two = {"name": "mouse"}


results = collection.find()
for r in results:
    print(r)