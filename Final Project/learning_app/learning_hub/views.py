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
    question.qtype = get_enum(form['qtype'].data, "question", "type")
    question.level = get_enum(form['level'].data, "question", "complexity")
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
        questions[number] = [q.id, q.question_title, q.question_text, q.qtype.value,
                             q.notion.notion,
                             q.level.value]
    return questions


@learning_hub_bp.route("/create_exam", methods=['POST', 'GET'])
def create_exam():
    form = request.form
    questions = get_list_of_questions(form)
    exam = models.Exams()
    exam.exam_title = form['exam_title']
    exam.exam_type = get_enum(form['type'], "exam", "type")
    exam.level = get_enum(form['level'], "exam", "complexity")
    notion = models.Notions(form["notion"])
    exam.notion = notion.isnotion()
    sub_notion = models.SubNotions(form["sub_notion"])
    exam.sub_notion = sub_notion.issubnotion()
    exam.time_for_completion = form['time']
    for q in questions:
        exam.questions.append(q)
    db.session.add(exam)
    db.session.commit()

    return redirect(url_for("hub.learning_hub_main"))


def get_enum(enum_param, content, type):
    """
    get the enum of the parameter -
    :param enum_param: string returned from front end form that defines the enum name
    :param content: questions or exam
    :param type: type of required enum
    :return: relevant enum
    """

    if content == "exam" and type == "type":
        if type == "type":
            for e_num in enums.ExamType:
                if e_num.name == enum_param:
                    return e_num

    elif content == "question" and type == "type":
        for e_num in enums.QuestionType:
            if e_num.name == enum_param:
                return e_num
    else:
        for e_num in enums.QuestionComplexity:
            if e_num.name == enum_param:
                return e_num


def get_list_of_questions(form):
    list_of_ids = []
    for key, value in form.items():
        if "q_ID_" in key:
            list_of_ids.append(value)

    questions = models.Questions.query.filter(models.Questions.id.in_(list_of_ids)).all()
    return questions


@learning_hub_bp.route("/delete_exam_show", methods=['POST', 'GET'])
def delete_exam_show():
    exams = {}

    return exams


@learning_hub_bp.route("/find_exam_to_delete", methods=['POST', 'GET'])
def find_exams_to_delete():
    string_to_search = request.json
    exams = models.Exams.query.filter(models.Exams.exam_title.contains(string_to_search)).all()
    response = {}
    for number, e in enumerate(exams):
        response[number] = [e.id, e.exam_title, e.exam_type.value, e.notion.notion,
                            e.sub_notion.sub_notion, e.level.value]
    return response


@learning_hub_bp.route("/delete_exam", methods=['POST', 'GET'])
def delete_exam():
    for item in request.form:
        exam = models.Exams.query.filter_by(id=item).first()
        db.session.delete(exam)
    db.session.commit()

    return redirect(url_for("hub.learning_hub_main"))


@learning_hub_bp.route("/find_notions", methods=['POST', 'GET'])
def find_notions():
    response = {}
    notions = models.Notions.query.all()
    for number, n in enumerate(notions):
        response[number] = [n.id,"notion", n.notion]
    save_index = len(response)

    sub_notions = models.SubNotions.query.all()
    for number, sn in enumerate(sub_notions):
        response[number + save_index] = [sn.id, "sub notion",sn.sub_notion]

    return response

@learning_hub_bp.route("/delete_notions", methods=['POST', 'GET'])
def delete_notions():

    form = request.form
    for key,id in request.form.items():
        if "sn" not in key:
            notion = models.Notions.query.filter_by(id=id).first()
            db.session.delete(notion)
        else:
            subnotion = models.SubNotions.query.filter_by(id=id).first()
            db.session.delete(subnotion)
        db.session.commit()
    return redirect(url_for("hub.learning_hub_main"))
