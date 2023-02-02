from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField,EmailField
from wtforms.validators import DataRequired,Length
from wtforms.widgets import TextArea

class CreateArticleForm(FlaskForm):
    title = StringField('Название',validators= [DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Отправить')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(),Length(max = 64, message='Максимальная длина никнейма - 64 символа')])
    password = PasswordField('Пароль', validators=[DataRequired(),Length(min = 6,max = 32, message='Длина пароля от 6 до 32 символов')])
    email = EmailField('E-mail', validators=[DataRequired(),Length(max = 128, message='Максимальная длина email - 128 символов')])
    submit = SubmitField('Отправить')
