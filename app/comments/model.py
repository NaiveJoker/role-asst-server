from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)

    def __init__(self, username, content):
        self.username = username
        self.content = content

    def getAll(self):
        return self.query.all()

    def add(self, comment):
        db.session.add(comment)
        return session_commit()

    def output(self, comment):
        return {
            'username': comment.username,
            'content': comment.content,
        }


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
