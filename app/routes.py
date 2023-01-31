from app import app
from flask import render_template,request
from app.forms import *
from app.models import *

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create_article', methods = ['GET', 'POST'])
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
    return render_template("create_article.html",form = form)




@app.route('/<username>')
def profile(username):
    return render_template("profile.html", message = username)
