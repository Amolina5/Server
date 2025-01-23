from flask import Flask, request
import json
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


products = []

def fix_id(obj):
    obj["id"] = str(obj["_id"])
    return obj


@app.get("/api/products")
def get_products():
    results = []
    cursor = db.products.find({})
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)
    


@app.post("/api/products")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    product = fix_id(product)
    return json.dumps(product)


@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {index}")

    if 0 <= index <= len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"


@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete: {index}")

    if index >= 0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist"
    

@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    coupon = fix_id(coupon)
    return json.dumps(coupon)

@app.get("/api/coupons")
def get_coupons():
    results = []
    cursor = db.coupons.find({})
    for coupon in cursor:
        results.append(fix_id(coupon))

    return json.dumps(results)




app.run(
    debug=True,
)  # that when i save the code, the changes are applied in to the server