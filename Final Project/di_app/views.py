import flask
import requests
import mistune
from . import syllabus as syl
from . import forms, models, create_user
from . import db
from . import login_manager
import flask_login  # LoginManager, login_user, login_required, logout_user, current_user
from flask import request, flash, redirect, session

# global parameter that initializes and downloads the syllabus of DI learning
syllabus = syl.Syllabus()

main_blueprint = flask.Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    """
    home page, shows the list of courses
    :return:
    """
    return flask.render_template('home.html', list_of_courses=syllabus.list_of_courses, course_data=syllabus.syllabuses)


# ----------------------login/out----------------------------------
# @main_blueprint.route("/login_show")
# def login_show():
#     form = forms.Login()
#     if "user" in session:
#         return redirect("/profile")
#     else:
#         return flask.render_template("login.html", form=form)
#
#
# @main_blueprint.route("/login", methods=['POST', "GET"])
# def login():
#     # check if user in the DB:
#     form = forms.Login()
#     user = models.User.query.filter_by(email=form.email.data).first()
#     if user:
#         if user.password == form.password.data:
#             session["user"] = user.username
#             session['user_email'] = user.email
#             session['role'] = user.role
#             flash("login complete, great success!")
#             flask_login.login_user(user)
#             return flask.render_template("/home.html", user=user, list_of_courses=syllabus.list_of_courses,
#                                          course_data=syllabus.syllabuses)
#         else:
#             flask.flash("password is in correct")
#             return redirect("/login_show")
#     else:
#         flask.flash("user doesn't exists, try again or sign in")
#         return redirect("/login_show")
#
#
# @main_blueprint.route("/signin_show")
# def signin_view():
#     form = forms.CreateUser()
#     return flask.render_template("signin.html", form=form)
#
#
# @main_blueprint.route("/signin", methods=['POST', "GET"])
# def signin():
#     form = forms.CreateUser()
#     user = models.User.query.filter_by(username=form.username.data).first()
#     if user:
#         if user.email == form.email.data:
#             flask.flash("email is taken, please use another")
#         elif user.username == form.email.data:
#             flask.flash("username is taken, please use another")
#     else:
#         new_user = models.User(email=form.email.data, password=form.password.data,
#                                username=form.username.data, name=form.name.data, role=form.role.data)
#         db.session.add(new_user)
#         db.session.commit()
#         # todo add check the user creation function
#         print("user created successfully")
#         flask.flash("user created successfully")
#
#         return redirect("/")
#
#     return flask.redirect("/")
#
#
# @main_blueprint.route("/signout", methods=['POST', "GET"])
# def signout():
#     session.clear()
#     return flask.redirect("/")
#
#
# @main_blueprint.route("/password_forget")
# # ----------------------end of login/out----------------------------------

# #-----------------------Start of user profile pages ----------------------
@main_blueprint.route('/profile/')
@flask_login.login_required
def profile():
    # get the user from the DB.
    user = models.User.query.filter_by(email=session['email']).first()
    return flask.render_template('profile.html', user=user)


# #-----------------------End of user profile pages ----------------------

# # ----------------------start of management area----------------------------------
@main_blueprint.route("/management")
@flask_login.login_required
def management_home_page():
    if session['role'] not in ('admin', 'teacher'):
        return flask.redirect("/")
    else:
        form = forms.CreateUser()
        return flask.render_template("management_home.html", sign_up_form=form)


@main_blueprint.route("/find_user", methods=['POST', "GET"])
def find_user():
    user_email = ""
    if request.method == "POST":
        user_email = request.json
        user = models.User.query.filter_by(email=session['user_email']).first()

        return {"email": user.email, "name": user.name, 'username': user.username, "role": user.role,
                "user_id": user.id}
    return user_email


@main_blueprint.route("/update_user", methods=['POST', 'GET'])
def update_user():
    form = request.form
    user = models.User.query.filter_by(id=request.form['user_id']).first()
    user.name = form['name']
    user.email = form['email']
    user.role = form['role']
    user.username = form['username']
    db.session.commit()

    return redirect("/management")


@main_blueprint.route("/delete_user", methods=['POST', 'GET'])
def delete_user():
    email = request.form['d_email']
    user = models.User.query.filter_by(email=email).first()
    db.session.delete(user)
    db.session.commit()

    return redirect("/management")


# # ----------------------end of management area----------------------------------

# # ----------------------start of course data show----------------------------------

@main_blueprint.route('/course/<course>')
@flask_login.login_required
def weeks(course):
    """
    Syllabus of a specific course
    :param course:
    :return:
    """
    return flask.render_template('weeks.html', data=syllabus.syllabuses[course]['weeks'], course=course)


@main_blueprint.route("/course/<course>/<week>")
@flask_login.login_required
def days(course, week):
    """
    View of a specific week of a specific course

    :param course:
    :param week:
    :return:
    """
    days_data = syllabus.syllabuses[course]['weeks'][week]['Days']
    others = syllabus.syllabuses[course]['weeks'][week]['other resources']
    return flask.render_template("days.html", data=days_data, others=others, course=course, week=week)


@main_blueprint.route("/course/<course>/<week>/<day>/<file>")
@flask_login.login_required
def render_file(course, week, day, file):
    """
    Download and view the contend of a course file.
    :param course:
    :param week:
    :param day:
    :param file:
    :return:
    """
    file_path = syllabus.get_file_path(course, week, day, file)
    try:
        cont = syllabus.repo.get_contents(file_path)
    except:
        flask.flash("The requested file is not available, please contact administrator", "missing file")
        return days(course, week)
    else:
        r = requests.get(cont.download_url)
    return flask.render_template("exercise.html", data=mistune.markdown(r.text), course=course, week=week, day=day,
                                 file=file)


# # ----------------------end of course data show----------------------------------


# # ----------------------start of error routes------------------------------------#
@main_blueprint.route('/getout')
@login_manager.unauthorized_handler
def unauthorized():
    return "This place is not for you, please leave"

# # ----------------------End of error routes------------------------------------#
