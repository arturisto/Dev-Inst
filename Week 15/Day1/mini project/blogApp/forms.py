import flask_wtf
import wtforms


class BlogForm(flask_wtf.FlaskForm):
    headline = wtforms.StringField("Headline", validators=[wtforms.validators.InputRequired()])
    blog_body = wtforms.TextAreaField('Text', render_kw={"rows": 10, "cols": 70},
                                      validators=[wtforms.validators.InputRequired()])
    tags = wtforms.StringField("Headline")
    submit = wtforms.SubmitField("Submit")
