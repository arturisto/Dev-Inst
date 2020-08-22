import flask, flask_login
from .. import db
from flask import request, flash, redirect, session, url_for, current_app, render_template
from . import user_blueprint
from . import forms, models
from ..static.enums import UserType
from ..static import constant_functions as const_func
import jwt


# ----------------------login/out----------------------------------
@user_blueprint.route("/login_show")
def login_show():
    form = forms.Login()
    if "user" in session:
        return redirect("/profile")
    else:
        return render_template("login.html", form=form)


@user_blueprint.route("/login", methods=['POST', "GET"])
def login():
    # check if user in the DB:
    form = forms.Login()
    user = models.User.query.filter_by(email=form.email.data).first()
    if user:
        if user.password == form.password.data:
            session["user"] = user.username
            session['user_email'] = user.email
            session['role'] = user.role
            flash("login complete, great success!")
            flask_login.login_user(user)
            return redirect(url_for("main.index"))
        else:
            flask.flash("password is in correct")
            return redirect("/login_show")
    else:
        flask.flash("user doesn't exists, try again or sign in")
        return redirect("/login_show")


@user_blueprint.route("/signin_show")
def signin_view():
    form = forms.CreateUser()
    return render_template("signin.html", form=form)


# todo - dissable this function when platform is complete - only for testing!!
@user_blueprint.route("/signup", methods=['POST', "GET"])
def signup():
    form = forms.CreateUser()
    user = models.User.query.filter_by(username=form.username.data).first()
    if user:
        if user.email == form.email.data:
            flash("email is taken, please use another")
        elif user.username == form.email.data:
            flash("username is taken, please use another")
    else:
        user_role = ''
        for key in UserType:
            if key.name == form.role.data:
                user_role = key

        new_user = models.User(email=form.email.data, password=form.password.data,
                               username=form.username.data, name=form.name.data, role=user_role)
        db.session.add(new_user)
        db.session.commit()
        # todo add check the user creation function

        flash("user created successfully")

        return redirect(url_for("main.index"))

    return redirect(url_for("main.index"))


@user_blueprint.route("/signout", methods=['POST', "GET"])
def signout():
    session.clear()
    return redirect(url_for("main.index"))


@user_blueprint.route("/password_forget")
def renew_password():
    return render_template("renew_pass.html")


@user_blueprint.route("/send_pass_link", methods=['POST', "GET"])
def send_pass_link():
    user = models.User.query.filter_by(email=request.form['email']).first()
    user.send_pass_link()
    return redirect(url_for("main.index"))


@user_blueprint.route("/reset_password")
def reset_password():
    token = request.args['jwt_token']
    user = verify_access_token(token)
    if not user:
        pass
    else:
        form = forms.password_reset()
        return flask.render_template("reset_password.html", form=form, email=user.email)


@user_blueprint.route("/change_password", methods=['POST', "GET"])
def change_password():
    form = request.form
    try:
        user = models.User.query.filter_by(email=form['email']).first()
        user.password = form['password']
        db.session.commit()
        flask.flash("password changed successfully")
    except Exception as e:
        print(e)
        return None

    return redirect(url_for("main.index"))


def verify_access_token(token):
    try:
        user_id = jwt.decode(token,
                             key=current_app.config['SECRET_KEY'])
    except Exception as e:
        print(e)
        return None
    return models.User.query.filter_by(id=user_id['user_id']).first()


# # ----------------------end of login/out----------------------------------

# #-----------------------Start of user profile pages ----------------------
# @main_blueprint.route('/profile/')
# @flask_login.login_required
# def profile():
#     # get the user from the DB.
#     user = models.User.query.filter_by(email=session['email']).first()
#     return flask.render_template('profile.html', user=user)
#
#
# # #-----------------------End of user profile pages ----------------------
#
# # # ----------------------start of management area----------------------------------
@user_blueprint.route("/management")
@flask_login.login_required
def management_home_page():
    if const_func.check_role(UserType.ADMIN):
        form_create_user = forms.CreateUser()
        return flask.render_template("management_home.html", sign_up_form=form_create_user,
                                     student_list=set_students_as_Choices())

    else:
        return flask.redirect(url_for("main.index"))


def set_students_as_Choices():
    students = models.User.query.filter_by(role=UserType.STUDENT).all()
    students_to_assign = {}
    for s in students:
        if not s.class_id:
            students_to_assign[s.id] = [s.name, s.email]
    return students_to_assign


@user_blueprint.route("/find_user", methods=['POST', "GET"])
def find_user():
    user_email = ""
    if request.method == "POST":
        user_email = request.json
        user = models.User.query.filter_by(email=user_email).first()
        response = {"email": user.email, "name": user.name, 'username': user.username, "role": user.role,
                    "user_id": user.id}
        return response
    return user_email


@user_blueprint.route("/update_user", methods=['POST', 'GET'])
def update_user():
    form = request.form
    user = models.User.query.filter_by(id=request.form['user_id']).first()
    user.name = form['name']
    user.email = form['email']
    user.role = form['role']
    user.username = form['username']
    db.session.commit()
    return redirect(url_for("users.management_home_page"))


@user_blueprint.route("/delete_user", methods=['POST', 'GET'])
def delete_user():
    email = request.form['d_email']
    user = models.User.query.filter_by(email=email).first()
    db.session.delete(user)
    db.session.commit()

    return redirect("/management")


@user_blueprint.route("/create_new_class", methods=['POST', 'GET'])
def create_new_class():
    form = request.form
    student_list = []
    for key, value in form.items():
        if "student_" in key:
            student_list.append(models.User.query.filter_by(id=form[key]).first())

    new_class = models.Class(class_name=form['class_name'], users=student_list)
    db.session.add(new_class)
    db.session.commit()
    return redirect(url_for("main.index"))


@user_blueprint.route("/find_class", methods=['POST', 'GET'])
def find_class():
    class_name = request.json
    class_data = models.Class.query.filter_by(class_name=class_name).first()
    response = {class_name: []}
    for user in class_data.users:
        response[class_name].append((user.id, user.name, user.email))
    return response


@user_blueprint.route("/delete_student", methods=['POST', 'GET'])
def delete_student():
    students_to_remove_from_class = request.form
    students_to_remove_from_class = students_to_remove_from_class.to_dict(flat=False)
    class_name = students_to_remove_from_class["class_name"]
    del students_to_remove_from_class["class_name"]
    for key, value in students_to_remove_from_class.items():
        user = models.User.query.filter_by(id=value[0]).first()
        user.class_id = None
        db.session.commit()

    check_delete_class(class_name)

    return redirect(url_for("main.index"))


def check_delete_class(class_name):
    student_class = models.Class.query.filter_by(class_name=class_name[0]).first()

    if not student_class.users:
        db.session.delete(student_class)
        db.session.commit()
