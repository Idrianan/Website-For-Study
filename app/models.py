from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True)
    password_hash = db.Column(db.String(64), index = True)
    email = db.Column(db.String(128), index = True)
    role = db.Column(db.String(16), index = True)

    def set_password(self,password:str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self,password:str) -> bool:
        return check_password_hash(self.password_hash,password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    text = db.Column(db.String(10000), index=True)

