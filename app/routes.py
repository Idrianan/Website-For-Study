from app import app
from flask import render_template,request,url_for,redirect,flash
from flask_login import current_user,login_user,logout_user,login_required
from app.forms import *
from app.models import *


@app.route('/')
@login_required
def index():
    return render_template("index.html")


@app.route('/create_article', methods = ['GET', 'POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if request.method == 'POST' and form.validate:
        a = Article(title = form.title.data, text = form.text.data)
        db.session.add(a)
        db.session.commit()
        return form.title.data
    art = Article.query.all()
    for i in art:
        print(i.title,i.text)
    return render_template("create_article.html", form = form, title = 'Создание статьи')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not(user.check_password_hash(form.password.data)):
            flash("Неверный логин или пароль")
            print('a')
            return render_template("login.html", form = form, title = 'Авторизация',err = 'Неверный логин или пароль')
        login_user(user)
        return redirect(url_for('index'))
    return render_template("login.html", form = form, title = 'Авторизация')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate:
        u = User(username = form.username.data, email = form.email.data, role = 'user')
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        login_user(u)
        return redirect(url_for("index"))
    return render_template("register.html", form = form, title = 'Регистрация')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


