import json
import textwrap

import flask
from flask import session, redirect, request

app = flask.Flask("TestApp")
app.secret_key = 'the random string'
cart = []

f = open("database/products.json", "r")
products = json.load(f)
f.close()
app.jinja_env.globals.update(textwrap=textwrap)


@app.route('/products')
def lesson():
    return flask.render_template("products.html", products=products)


@app.route('/products/<product_name>')
def product(product_name):
    for item in products:
        if product_name == item['Name']:
            return flask.render_template("product.html", product=item)
    else:
        return False


@app.route("/products/add_to_cart")
def add_to_cart():
    for item in products:
        if request.args["productId"] == item['ProductId']:
            cart.append(item)

    return redirect("/products")


@app.route("/shoppingCart")
def show_shopping_cart():
    return flask.render_template("/shopcart.html", cart=cart)


app.run()
