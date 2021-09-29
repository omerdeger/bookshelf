from datetime import datetime
from app import db


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    books = db.relationship('Book', backref='author', lazy=True)
    
    def __repr__(self):
        return f'Author({self.name}, {self.surname}'

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    ISBN_10 = db.Column(db.Integer())
    ISBN_13 = db.Column(db.Integer())
    image_file = db.Column(db.String(255), default='default-book.png')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'Book({self.name}, {self.description}'

class Bookshelf(db.Model):
    __tablename__ = 'bookshelf'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(255))
    bookshelfcolor = db.Column(db.String(15), default='azure')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<BookShelf %r>' % self.title

