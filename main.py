from flask import Flask, request
from models.product import Product
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    import os
    h = os.getenv("XDG_DATA_HOME")
    return "Hello from flask " + h

@app.route("/products")
def prods():
    p = Product.select()
    return {"products": [model_to_dict(pr) for pr in p]}

@app.route("/products/new")
def prods_new():
    p = Product()
    p.name = request.args.get("name")
    p.price = request.args.get("price")
    p.save()

    return "Created"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
