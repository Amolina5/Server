from flask import Flask, request, jsonify
import json
import pymongo
from bson import ObjectId
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "Hello from the test page"

@app.get("/about")
def about():
    return "Alex Molina"

@app.get("/hello")
def hello():
    message = {"message": "Hello there!"}
    return json.dumps(message)

products = []  # Keep for backwards compatibility

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def get_products():
    results = []
    cursor = db.products.find({})
    for prod in cursor:
        results.append(fix_id(prod))
    print("Products fetched successfully")
    return json.dumps(results)

@app.post("/api/products")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    product = fix_id(product)
    print("Product saved successfully")
    return json.dumps(product)

@app.put("/api/products/<id>")
def update_product(id):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {id}")
    
    result = db.products.update_one(
        {"_id": ObjectId(id)}, 
        {"$set": updated_product}
    )
    
    if result.modified_count > 0:
        print("Product updated successfully")
        return json.dumps(updated_product)
    else:
        print("That product does not exist")
        return "That product does not exist"

@app.delete("/api/products/<id>")
def delete_product(id):
    print(f"delete: {id}")
    
    result = db.products.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count > 0:
        print("Product deleted successfully")
        return json.dumps({"message": "Product deleted"})
    else:
        print("That product does not exist") 
        return "That product does not exist"



@app.post("/api/coupons")
def save_coupons():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    print("Coupon saved successfully")
    return json.dumps(coupon)

@app.get("/api/coupons")
def read_coupons():
    results = []
    cursor = db.coupons.find({})
    for cp in cursor:
        results.append(fix_id(cp))
    print("Coupons fetched successfully")
    return json.dumps(results)

app.run(debug=True)