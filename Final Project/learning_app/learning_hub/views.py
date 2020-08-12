import flask, flask_login
import requests
from .. import db, login_manager
from flask import request, flash, redirect, session, url_for, current_app, render_template
from . import learning_hub_bp
from . import forms, models
from ..static import constant_functions as const_func
from ..static import enums
import jwt


@learning_hub_bp.route("/main")
def learning_hub_main():
    if const_func.check_role(enums.UserType.ADMIN) or const_func.check_role(enums.UserType.TEACHER):
        quest_form = forms.CreateQuestion()
        exam_form = forms.CreateExam()
        return flask.render_template("content_management.html", quest_form=quest_form, exam_form=exam_form)
    else:
        return redirect("main.index")


@learning_hub_bp.route("/create_quest", methods=["POST", "GET"])
def create_quest():
    form = forms.CreateQuestion(request.form)

    question = models.Questions()
    notion = models.Notions(form.notion.data)
    form.notion.data = notion.isnotion()
    sub_notion = models.SubNotions(form.sub_notion.data)
    form.sub_notion.data = sub_notion.issubnotion()
    form.populate_obj(question)
    db.session.add(question)
    db.session.commit()
    return redirect(url_for("hub.learning_hub_main"))


@learning_hub_bp.route("/delete_quest", methods=['POST', 'GET'])
def find_questions_to_delete():
    string_to_search = request.json
    questions = models.Questions.query.filter(models.Questions.question_title.contains(string_to_search)).all()
    response = {}
    for number, q in enumerate(questions):
        response[number] = [q.id, q.question_title, q.question_text, enums.QuestionType[q.qtype].value, q.notion.notion,
                            q.sub_notion.sub_notion, enums.QuestionComplexity[q.level].value]
    return response


@learning_hub_bp.route("/delete_questions", methods=['POST', 'GET'])
def delete_questions():
    for item in request.form:
        question = models.Questions.query.filter_by(id=item).first()
        db.session.delete(question)
    db.session.commit()

    return redirect(url_for("hub.learning_hub_main"))


@learning_hub_bp.route("/get_questions_for_exam", methods=['POST', 'GET'])
def get_questions_for_exam():
    db_questions = models.Questions.query.all()
    questions = {}
    for number, q in enumerate(db_questions):
        questions[number] = [q.id, q.question_title, q.question_text, enums.QuestionType[q.qtype].value,
                             q.notion.notion,
                             enums.QuestionComplexity[q.level].value]
    return questions

@learning_hub_bp.route("/create_exam", methods=['POST', 'GET'])
def create_exam():
    form = request.form
    questions = get_list_of_questions(form)
    exam = models.Exams()

    notion = models.Notions(form["notion"])
    exam.notion = notion.isnotion()
    sub_notion = models.SubNotions(form["sub_notion"])
    exam.sub_notion = sub_notion.issubnotion()
    for q in questions:
        exam.questions.append(q)
    db.session.add(exam)
    db.session.commit()

    return redirect(url_for("hub.learning_hub_main"))


def get_list_of_questions(form):
    list_of_ids = []
    for key,value in form.items():
        if "q_ID_" in key:
            list_of_ids.append(value)

    questions = models.Questions.query.filter(models.Questions.id.in_(list_of_ids)).all()
    return questions

@learning_hub_bp.route("/delete_exam", methods=['POST', 'GET'])
def delete_exam():


    return redirect(url_for("hub.learning_hub_main"))