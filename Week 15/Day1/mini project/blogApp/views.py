import os
import flask
from flask import request, flash, session
from . import app, db, model, forms
from datetime import date


@app.route("/index")
def home():

    if session['user']:
        blogs = model.Blog.query.all()
        return flask.render_template("index.html", blogs=blogs)

    else:
        return flask.render_template("index.html")


@app.route("/login_show")
def login_show():
    return flask.render_template("login.html")


@app.route("/login", methods=['POST', "GET"])
def login():
    # check if user in the DB:
    user = model.User.query.filter_by(username=request.form['username']).first()
    if user:
        if user.password == request.form['password']:
            session["user"] = user.username
            session['user_email'] = user.email
            flash("login complete, great success!")
            return flask.render_template("landing1.html", user=user)

        else:
            flask.flash("password is in correct")
            return flask.render_template("login.html")
    else:
        flask.flash("user doesn't exists, try again or sign in")
        return flask.render_template("login.html")


@app.route("/signin_show")
def signin_view():
    return flask.render_template("signin.html")


@app.route("/signin", methods=['POST', "GET"])
def signin():
    user = model.User.query.filter_by(email=request.form['email']).first()
    if user:
        if user.email == request.form['email']:
            flask.flash("email is taken, please use another")
        elif user.username == request.form['username']:
            flask.flash("username is taken, please use another")
    else:
        new_user = model.User(email=request.form['email'], password=request.form['password'],
                              username=request.form['username'])
        db.session.add(new_user)
        db.session.commit()
        return flask.render_template("landing1.html", user=user)

    return flask.redirect("/index")


@app.route("/signout", methods=['POST', "GET"])
def signout():
    session.clear()
    return flask.redirect("/index")


@app.route("/create_new_blog", methods=['POST', 'GET'])
def create_blog_entry():
    form = forms.BlogForm()
    return flask.render_template("new_blog.html", form=form)


@app.route("/post_blog", methods=['POST', 'GET'])
def post_blog():
    headline = request.form["headline"]
    blog_text = request.form["blog_body"]
    all_tags = model.Tags.query.all()
    if request.form['tags']:
        tags_input = request.form['tags'].split(",")
        blog_entry = model.Blog(blog=request.form['blog_body'],
                                blog_headline=request.form['headline'],
                                user_email=session['user_email'],
                                publising_date=date.today())
        for tag in tags_input:
            db_tag = model.Tags.query.filter_by(tag_name=tag).first()
            if db_tag:
                blog_entry.tags.append(db_tag)
                db.session.add(db_tag)
            else:
                tag_model = model.Tags(tag_name=tag)
                blog_entry.tags.append(tag_model)
                db.session.add(tag_model)

        db.session.add(blog_entry)

    else:
        blog_entry = model.Blog(blog=request.form['blog_body'],
                                blog_headline=request.form['headline'],
                                user_email=session['user_email'],
                                publising_date=date.today())
        db.session.add(blog_entry)

    db.session.commit()
    print(headline)
    print(blog_text)
    return flask.redirect("/index")

def get_most_commog_tag():

    user = model.User.query.filter_by(username=session['user']).first()
    tags = {}

    for blog in user.blog:
        for tag in blog.tags:
            if tag.tag_name in tags:
                tags[tag.tag_name]+=1
            else:
                tags[tag.tag_name] = 1
    most_commot_tag = ""
    max_occurences = 0
    for tag,amount in tags.items():
        if amount >max_occurences:
            most_commog_tag = tag
            max_occurences=amount

    return (most_commog_tag, len(user.blog))

    pass
@app.route("/profile")
def profile():
    most_common_tag,num_of_posts = get_most_commog_tag()

    return flask.render_template("profile.html", common_tag = most_common_tag, num_of_posts=num_of_posts)