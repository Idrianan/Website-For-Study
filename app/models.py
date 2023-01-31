from app import db

class User:
    pass

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    text = db.Column(db.String(10000), index=True)

