from flask              import current_app
from flask_wtf          import FlaskForm
from wtforms            import StringField,SubmitField,SelectField,TextAreaField,HiddenField
from wtforms.widgets    import TextArea
from wtforms.validators import DataRequired

class articleForm(FlaskForm):
    title          = StringField("Title",[DataRequired("Article title required")])
    content        = HiddenField("Content",[DataRequired("Content required")],id="content")
    associate_page = StringField("Page")
    submit         = SubmitField()

class chooseArticleForm(FlaskForm):
    title          = SelectField("Title",[DataRequired("Article title required")])
    submit         = SubmitField()
