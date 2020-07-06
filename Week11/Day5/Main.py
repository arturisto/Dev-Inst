import json
import os
import textwrap

import flask
from flask import session, redirect, request, flash
from werkzeug.utils import secure_filename

app = flask.Flask("TestApp")
app.secret_key = 'the random string'
cart = []
categories = {"main_category": set(), "category": set()}

f = open("database/products.json", "r")
products = json.load(f)
f.close()
app.jinja_env.globals.update(textwrap=textwrap)
UPLOAD_FOLDER = "D:\Developers Institute\git\Week11\Day5\static\img"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
for item in products:
    categories["main_category"].add(item['MainCategory'])
    categories["category"].add(item["Category"])


@app.route('/home')
def products_show():
    return flask.render_template("products.html", products=products)


@app.route('/products/<product_name>')
def product(product_name):
    for item in products:
        if product_name == item['Name']:
            return flask.render_template("product.html", product=item)
    else:
        return False


@app.route("/home/add_to_cart")
def add_to_cart():
    for item in products:
        if request.args["productId"] == item['ProductId']:
            cart.append(item)

    return redirect("/home")


@app.route("/shoppingCart")
def show_shopping_cart():
    return flask.render_template("/shopcart.html", cart=cart)


@app.route("/addNewProduct")
def add_new_product():
    return flask.render_template("/newproduct.html", categories=categories)


@app.route("/proccessNewProduct", methods=['POST', 'GET'])
def process_new_product():
    if request.method == "POST":
        if check_id(request):
            pass

    return redirect("/home")


def check_id(req):
    form = dict(req.form)

    for product in products:
        if product["ProductId"] == form["id"]:
            break
    else:
        new_product = {"ProductId": form["id"],
                       "Category": form["category"],
                       "MainCategory": form["main_category"],
                       "SupplierName": form["sup_name"],
                       "Description": form["description"],
                       "Name": form["name"],
                       "ProductPicUrl": "img/" + req.files["image"].filename,
                       "Status": "Available",
                       "Quantity": form["stock"],
                       "UoM": "PC",
                       "CurrencyCode": form["currency"],
                       "Price": form["price"]}
        products.append(new_product)

        file = req.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        with open("database/products.json", "w") as file:
            json.dump(products, file)


app.run()
