import os
import flask
from flask import request, flash, redirect, session
from ShoeStore import app
import json
import datetime
import random

shoes_file = os.path.join(app.static_folder, 'database.json')
carts_file_path = os.path.join(app.static_folder, 'carts.json')
confirmed_orders_path = os.path.join(app.static_folder, 'confirmed_orders.json')
users_path = os.path.join(app.static_folder, 'users.json')
app.config["SECRET_KEY"] = "123456789"


@app.route("/home")
def index():
    with open(shoes_file) as file:
        stores_db = json.load(file)["stores"]
        list_of_stores = []
        for store in stores_db:
            list_of_stores.append(store["city"])
        return flask.render_template("home.html", cities=list_of_stores)


@app.route('/chosen_store', methods=['GET', 'POST'])
def go_to_main():
    if request.method == "POST":
        chosen_city = request.form['city']
        with open(shoes_file) as file:
            db_file = json.load(file)
            stores = db_file["stores"]
            for store in stores:
                if store['city'] == chosen_city:
                    data_to_render = create_load_data(store["shoes_available"], db_file["products"])
                    session['city'] = chosen_city
                    session['data'] = data_to_render
                    return flask.render_template("main.html", data=data_to_render, city=chosen_city)
            else:
                flash("An error occurred, please try again")
                return redirect("/home")


def create_load_data(store, products):
    data = []
    for item in store:
        if item['num available'] > 0:
            single_shoe_data = arrange_data(get_product_data(item["id"], products), item)
            data.append(single_shoe_data)
    return data


def get_product_data(id, products):
    for item in products:
        if item["id"] == id:
            return item
    return None


def arrange_data(shoe, store):
    data_to_print = {"colors": store["colors_available"], "brand": shoe["brand"], "name": shoe["name"],
                     "price": shoe["price"], "img": shoe["img"], "available": store["num available"], "id": shoe['id']}
    return data_to_print


@app.route("/add_to_cart", methods=["POST", "GET"])
def update_cart():
    if request.method == 'POST':
        cart = dict(request.form)
        cart['city'] = session['city']
        with open(carts_file_path, "r+") as cart_file:
            if not cart_file.read(1):  # the file is empty
                data_to_dump = [cart]
            else:
                cart_file.seek(0)
                data_to_dump = json.load(cart_file)
                data_to_dump.append(cart)
                cart_file.seek(0)
            json.dump(data_to_dump, cart_file)
        return flask.render_template("main.html", data=session["data"], city=session['city'])


@app.route("/shoppingCart")
def show_cart():
    with open(carts_file_path, "r+") as cart_file:
        cart_data = json.load(cart_file)
        cart = []
        with open(shoes_file) as file:
            db_file = json.load(file)
            products = db_file["products"]
            for item in cart_data:
                product = get_product_data(int(item['id']), products)
                cart.append({"img": product["img"],
                             "color": item['color'],
                             "size": item['size'],
                             'amount': int(item['amount']),
                             'price': product['price'],
                             'name': product['name'],
                             'brand': product['brand']
                             })
    return flask.render_template("cart.html", cart=cart)


# the delivery date set's 7 -14 days from today
def get_delovery_date():
    return (datetime.datetime.now() + datetime.timedelta(days=random.randint(7, 14))).date()


@app.route("/checkout", methods=["POST", "GET"])
def convert_cart_to_order():
    delivery_date = get_delovery_date()
    with open(carts_file_path, "r+") as cart_file:
        cart_data = json.load(cart_file)
        order = {"name": request.form['name'],
                 "address": request.form['address'],
                 "delivery_date": str(delivery_date),
                 "order_data": []}

        for item in cart_data:
            order['order_data'].append({"color": item['color'],
                                        "size": item['size'],
                                        'amount': int(item['amount']),
                                        "id": int(item['id'])
                                        })

    with open(confirmed_orders_path, "r+") as orders_file:
        if not orders_file.read(1):  # the file is empty
            json.dump([order], orders_file)
        else:
            orders_file.seek(0)
            data_to_dump = json.load(orders_file)
            data_to_dump.append(order)
            orders_file.seek(0)
            json.dump(data_to_dump, orders_file)

        flash("order was created successfully")
        flash(f"the order will be delivered by{delivery_date}")
    decrease_stock(order)

    # clear cart
    with open(carts_file_path, "w") as file:
        pass

    return redirect("/home")


def decrease_stock(order):
    db_stock = ''
    with open(shoes_file, "r") as db_shoes:
        db_stock = json.load(db_shoes)
        if isinstance(order, dict):
            order = [order]
        for order_item in order[0]['order_data']:
            for i, store in enumerate(db_stock['stores']):
                if store["city"] == session["city"]:
                    for j, item in enumerate(store['shoes_available']):
                        if item["id"] == order_item['id']:
                            db_stock['stores'][i]['shoes_available'][j]["num available"] -= order_item['amount']

    with open(shoes_file, "w") as db_shoes:

        json.dump(db_stock, db_shoes)


@app.route("/login")
def login():
    return flask.render_template("/signin.html")


@app.route("/checkuser",methods=["POST", "GET"])
def check_users():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_cred(username, password):
            flash("login successfull")
            return redirect("/home")
        else:
            flash("username or password is incorrect")
            return redirect("/login")
    else:
        flash("I am sorry, I didn't understand your input. Please try again")

    return redirect("/login")


def find_user(username):
    with open(users_path, "r") as file:
        users = json.load(file)

        for user in users:
            if user["username"] == username:
                return True
        else:
            return False


def check_cred(username, password):
    with open(users_path, "r") as file:
        users = json.load(file)

        for user in users:
            if user["username"] == username:
                if user["password"] == password:
                    session["user"] = username
                    if user["admin"] == 'True':
                        session["admin"] = 'True'
                    else:
                        session['admin'] = 'False'
                    return True
                else:
                    return False
        else:
            return False
