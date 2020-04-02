from flask import Flask, jsonify, request
from DBConnection import DBConnection
import pymongo
import json
from bson.json_util import dumps
from bson import json_util, ObjectId, objectid
from datetime import datetime

app = Flask(__name__)

#TODO: refactor this to another file
try:
    my_conn = DBConnection("virtualspiceapp", "spice", "SpiceAdmin","SpiceAdmin123")
except pymongo.errors.OperationFailure:
    print("Authentication error: The Username or Password is not valid")

@app.route("/api/virtualspice")
def virtualspice():
    return dumps(my_conn.find_all_items_2())

@app.route("/api/virtualspice/<name>")
def get_foods_by_name(name):
    return dumps(my_conn.find_items_by_name(name))

@app.route("/api/virtualspice/delete/<id>")
def delete_foods_by_id(id):
    try:
        my_conn.delete_single_item_from_db(id)
        resp = jsonify(success=True)
        return resp
    except:
        resp = jsonify(success=False)
        return resp

@app.route("/api/virtualspice/delete/all")
def delete_all_foods():
    my_conn.delete_all_items_from_db()
    return None

@app.route("/api/getcountofallitems")
def get_number_of_all_items():
    return jsonify(my_conn.get_count_of_all_items())
    
@app.route("/api/getcountoftypes")
def get_count_of_types():
    return json.dumps(my_conn.counts_per_type())

@app.route("/api/shoppinglist")
def shoppinglist():
    return "shoppinglist"

@app.route("/api/recepies")
def recepies():
    return "recepies"

@app.route("/api/login")
def login():
    return "login"

if __name__ == "__main__":
    app.run(port=5000)
    


