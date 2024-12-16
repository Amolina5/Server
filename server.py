from flask import Flask
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

# Creat ab endpoint that says hello using a variable instead of using a string

app.run(debug=True)#that when i save the code the changes are applied in the sever