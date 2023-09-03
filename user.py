import json
from flask import Flask
from flask import jsonify
app = Flask(__name__)
from pymongo import MongoClient
data = request.json
client = MongoClient("mongodb://localhost:27017/")
collection = client["library"]["user"]
@app.route ("/users/", methods=["POST"])
def add():
    dict = {'email': data.get("email"),'user_name': data.get("user_name"), 'password': data.get("password")}
    print("this data is being added: ", dict)
    records= collection.insert_one(dict)
    return "account succsessfully made" 

@app.route('/users/')
def funtion():
    data = request.args.to_dict()
    print("The data are : ", data)
    print("The parameter is: ", type(data.get("user_name")))
    record = list(collection.find({"user_name": int(data.get("user_name"))},{"_id": 0}))
    return jsonify(record)
