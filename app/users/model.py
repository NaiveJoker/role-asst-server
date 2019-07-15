from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwd = db.Column(db.String(50), nullable=False)

    def __init__(self, username, email, passwd):
        self.username = username
        self.email = email
        self.passwd = passwd

    # 查询所有用户
    def getAll(self):
        return self.query.all()
    # 根据用户名查询用户

    def get_byname(self, username):
        return self.query.filter_by(username=username).first()

    def get_byemail(self, email):
        return self.query.filter_by(email=email).first()

    # 增加用户
    def add(self, user):
        db.session.add(user)
        return session_commit()

    # 更新用户
    def update(self):
        return session_commit()

    # 删除用户
    def delete(self, id):
        deleteRow = self.query.filter_by(user_id=id).delete()
        return session_commit()
    # 输出信息

    def output(self, user):
        return {
            'username': user.username,
            'email': user.email,
        }


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
