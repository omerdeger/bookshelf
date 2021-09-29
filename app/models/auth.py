from datetime import datetime
from app import db
from ..models.bookshelf import Bookshelf


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    bookshelfs = db.relationship('Bookshelf', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

