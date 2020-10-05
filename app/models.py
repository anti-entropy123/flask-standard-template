from . import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(50), primary_key=True)
    nickname = db.Column(db.String(30))
    avatar = db.Column(db.String(255))
    sex = db.Column(db.Boolean())
    mobile = db.Column(db.String(45))
    introduction = db.Column(db.String(45))
    