import flask_wtf
import wtforms as wtf
from wtforms import validators as valid
from wtforms.fields.html5 import EmailField
from ..static import enums


class CreateQuestion(flask_wtf.FlaskForm):
    """
    Form for create question
    """
    qtype = wtf.SelectField("Question Type", choices=[(type.name, type.value) for type in enums.QuestionType])
    question_title = wtf.StringField("Question Title", [valid.InputRequired(message="Title is required")])
    question_text = wtf.StringField("Question Body", [valid.InputRequired(message="Quieston body is required")],
                                    widget=wtf.widgets.TextArea())
    answer = wtf.StringField("Answer", [valid.InputRequired(message="Answer is required")])
    wrong_answer1 = wtf.StringField("Wrong Answer 1")
    wrong_answer2 = wtf.StringField("Wrong Answer 2")
    wrong_answer3 = wtf.StringField("Wrong Answer 3")
    notion = wtf.StringField("Notion")  # todo change to relationship with notion table
    sub_notion = wtf.StringField("Sub Notion")  # todo change to relationship with sub notion table
    is_exam = wtf.BooleanField("Is Exam")
    is_test_exam = wtf.BooleanField("Is Test Exam")
    level = wtf.SelectField("Complexity level", [valid.InputRequired(message="Complexity is required")],
                            choices=[(type.name, type.value) for type in enums.QuestionComplexity])
    time_for_completion = wtf.FloatField("Time for completion",
                                         render_kw={"placeholder": "Time in minutes"})  # todo - change to actual time
    submit = wtf.SubmitField('Register Question')


class Notion(flask_wtf.FlaskForm):
    notion = wtf.StringField("Enter New Notion", [valid.InputRequired(message="input is Required")])


class SubNotion(flask_wtf.FlaskForm):
    notion = wtf.StringField("Enter Notion", [valid.InputRequired(message="input is Required")])
    # todo change to relationship with notion table
    sub_notion = wtf.StringField("Enter new sub notion", [valid.InputRequired(message="input is Required")])


class CreateExam(flask_wtf.FlaskForm):
    type = wtf.SelectField("Exam Type", choices=[(type.name, type.value) for type in enums.ExamType])
    exam_title = wtf.StringField("Exam Title", [valid.InputRequired(message="input is Required")])
    notion = wtf.StringField("Enter Notion", [valid.InputRequired(message="input is Required")])
    sub_notion = wtf.StringField("Enter new sub notion")
    level = wtf.SelectField("Complexity level", [valid.InputRequired(message="Complexity is required")],
                            choices=[(type.name, type.value) for type in enums.QuestionComplexity])
    time = wtf.StringField("Exam time", render_kw={"placeholder": "Time in minutes"})  # todo - change to actual time
    submit = wtf.SubmitField('Register Exam')
