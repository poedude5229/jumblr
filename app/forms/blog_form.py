from flast_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileAllowed, FileField, FileRequired
from app.models import Blog

class BlogForm(FlaskForm):
    name = StringField("Blog Title: ", validators=[DataRequired()])
