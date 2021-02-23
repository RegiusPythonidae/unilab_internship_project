from db import db

class UserModel(db.Model):

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password = db.Column(db.String(64), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, name):
        user_to_find = UserModel.query.filter_by(username=name).first()

        if user_to_find is not None:
            return user_to_find
        else:
            return None

    @classmethod
    def find_by_userid(cls, userid):
        user_to_find = UserModel.query.filter_by(id=userid).first()

        if user_to_find is not None:
            return user_to_find
        else:
            return None

    @classmethod
    def add_user(cls, username, password):
        new_user = UserModel(username, password)
        db.session.add(new_user)
        db.session.commit()