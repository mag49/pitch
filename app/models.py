from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))


    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))





class USER:
    user = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def user(self):
        USER.all_user.append(self)


class PICKUPLINES:
    all_pickuplines = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_pickupline(self):
        PICKUPLINES.all_pickuplines.append(self)

    @classmethod
    def clear_pitchs(cls):
        PICKUPLINES.all_pickuplines.clear()
    @classmethod
    def get_pitchs(cls):
        response = []
        for pitchs in cls.all_pickuplines:
            response.append(pitchs)
        return response

class INTERVIEW:
    all_interview = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def save_interview(self):
        INTERVIEW.all_interview.append(self)

class BUSINESSPLAN:
    all_businessplan = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def save_businessplan(self):
        BUSINESSPLAN.all_businessplan.append(self)


class PITCH():
    all_pitch = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def save_businessplan(self):
        PITCH.pitch.append(self)



