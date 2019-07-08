from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
db = conn.stockdb
db.col.insert_one({"name":'yanying','province':'江苏','age':25})
