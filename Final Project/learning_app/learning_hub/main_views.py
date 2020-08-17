import flask, flask_login
import requests
from .. import db, login_manager
from flask import request, flash, redirect, session, url_for, current_app, render_template
from . import learning_hub_bp
from . import forms, models
from ..static import constant_functions as const_func
from ..static import enums
import jwt


@learning_hub_bp.route("/free-for-all")
def free_for_all_questions():
    return render_template("free_for_all_q.html")


@learning_hub_bp.route("/get_q_ids_free_for_all", methods=["POST", "GET"])
def get_q_ids_free_for_all():
    is_timed = request.json
    if is_timed:
        questions = models.Questions.query.filter(models.Questions.time_for_completion > "0",
                                                  models.Questions.is_exam == "0",
                                                  models.Questions.is_test_exam == "0").all()

    else:
        questions = models.Questions.query.filter(models.Questions.is_exam == "0",
                                                  models.Questions.is_test_exam == "0").all()

    return create_response(questions, is_timed)


@learning_hub_bp.route("/get_q_by_id", methods=["POST", "GET"])
def get_q_by_id():
    response = ""

    q = models.Questions.query.filter_by(id=request.json).first()

    if q.qtype == enums.QuestionType.SINGLE:
        response = {"id": q.id,
                    "title": q.question_title,
                    "body": q.question_text,
                    "answer": q.answer,
                    "type": q.qtype.value,
                    "notion": q.notion.notion,
                    "subnotion": q.sub_notion.sub_notion,
                    "level": q.level.value,
                    "time": q.time_for_completion}
    else:
        response = {"id": q.id,
                    "title": q.question_title,
                    "body": q.question_text,
                    "answer": q.answer,
                    "wrong1": q.wrong_answer1,
                    "wrong2": q.wrong_answer2,
                    "wrong3": q.wrong_answer3,
                    "type": q.qtype.value,
                    "notion": q.notion.notion,
                    "subnotion": q.sub_notion.sub_notion,
                    "level": q.level.value,
                    "time": q.time_for_completion}
    return response


@learning_hub_bp.route("/exe_by_notion", methods=["POST", "GET"])
def exe_by_notion():
    notions = models.Notions.query.all()
    subnotions = models.SubNotions.query.all()
    return render_template("exercise_by_notion.html", notions=notions, subnotions=subnotions)


@learning_hub_bp.route("/get_q_by_notion", methods=["POST", "GET"])
def get_q_by_notion():
    notion = models.Notions.query.filter_by(notion=request.json[0]).first()
    sub_notion = models.SubNotions.query.filter_by(sub_notion=request.json[1]).first()
    is_timed = request.json[2]
    if is_timed:
        questions = models.Questions.query.filter(models.Questions.time_for_completion > "0",\
                                                  models.Questions.is_exam == "0", \
                                                  models.Questions.is_test_exam == "0",\
                                                  models.Questions.notion_id == notion.id,\
                                                  models.Questions.sub_notion_id == sub_notion.id).all()

    else:
        questions = models.Questions.query.filter(models.Questions.is_exam == 0,\
                                                  models.Questions.is_test_exam == 0,\
                                                  models.Questions.notion_id == notion.id,\
                                                  models.Questions.sub_notion_id == sub_notion.id).all()

    if questions:
        return create_response(questions, is_timed)
    else:
        return "false"


def create_response(questions, timer):
    response = {}
    if timer:
        for number, q in enumerate(questions):
            response[number] = [q.id, q.time_for_completion]
    else:
        for number, q in enumerate(questions):
            response[number] = [q.id]
    return response
