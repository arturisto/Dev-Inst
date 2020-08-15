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
    response = {}

    questions = models.Questions.query.filter_by(is_exam="0", is_test_exam="0").all()

    for number, q in enumerate(questions):
        response[number] = [q.id, q.time_for_completion]
    return response


@learning_hub_bp.route("/get_q_by_id", methods=["POST", "GET"])
def get_q_by_id():
    response = ""

    q = models.Questions.query.filter_by(id=request.json).first()

    if q.qtype == enums.QuestionType.SINGLE:
        response = {"id": q.id,
                    "title":q.question_title,
                    "body":q.question_text,
                    "answer":q.answer,
                    "type":q.qtype.value,
                    "notion":q.notion.notion,
                    "subnotion":q.sub_notion.sub_notion,
                    "level":q.level.value,
                    "time":q.time_for_completion}
    else:
        response = {"id": q.id,
                   "title": q.question_title,
                   "body": q.question_text,
                   "answer": q.answer,
                   "wrong1":q.wrong_answer1,
                   "wrong2": q.wrong_answer2,
                   "wrong3": q.wrong_answer3,
                   "type": q.qtype.value,
                   "notion": q.notion.notion,
                   "subnotion": q.sub_notion.sub_notion,
                   "level": q.level.value,
                   "time": q.time_for_completion}
    return response
