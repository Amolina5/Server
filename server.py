from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello form flask"

@app.get("/test")
def test():
    return "hello from the test page"

@app.get("/about")
def about():
    return "Alex Molina"

@app.get("/hello")
def hello():
    message = {"message":"Hello there"}
    return json.dumps(message)

products = []

@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"this is my new product {product}")
    products.append(product)
    return json.dumps(product)

@app.put("/api/products/<int:index>")
def update_product(index):
    update_product = request.get_json()
    print(f"products: {update_product}: {index}")

    if 0 <= index <= len(products):
        products[index] = update_product
        return json.dumps(update_product)
    else:
        return "that index does not exist"

@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete: {index}")

    if index >=0 and index < len(products):
        delete_product = products.pop(index)
        return json.dumps(delete_product)
    else:
        return "That index does not exist"

    

# Creat ab endpoint that says hello using a variable instead of using a string

app.run(debug=True, port=8000)#that when i save the code the changes are applied in the sever