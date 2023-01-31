from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class CreateArticleForm(FlaskForm):
    title = StringField('Название',validators= [DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Отправить')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    pass