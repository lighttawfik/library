import json
from flask import Flask, request
from flask import jsonify
app = Flask(__name__)
 
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
collection = client["libary"]["books"]

@app.route ("/books/", methods=["POST"])
def add():
    data = request.json
    dict={
        "name":data.get("name"),
        "price":data.get("price"),
        "release_date":data.get("release_data"),
        "author":data.get("author"),
        "category":data.get("category")
    }
    records= collection.insert_one(dict)
    return "Adding book"
app.run(port=5001)




    

