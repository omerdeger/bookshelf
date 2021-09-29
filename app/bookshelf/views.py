from flask import render_template, request, redirect, url_for
from . import bookshelf
from .forms import BookForm, BookShelfForm
from ..models.bookshelf import Book, Bookshelf
from ..models.auth import User
from app import db


@bookshelf.route('/', methods=['GET', 'POST'])
def index():
    books = Book.query.all()
    bookshelfs = Bookshelf.query.all()
    bookshelf_form = BookShelfForm(request.form)

    if bookshelf_form.validate_on_submit():
        bookshelf = Bookshelf(title=bookshelf_form.title.data, 
                                description=bookshelf_form.description.data, 
                                bookshelfcolor=request.form['color'], 
                                user_id=1)
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for('bookshelf.index'))


    return render_template('bookshelf.html',
                            title='Uygulama',
                            books=books, 
                            bookshelfs=bookshelfs,
                            bookshelf_form=bookshelf_form)

@bookshelf.route('/<int:bookshelf_id>/delete', methods=['POST'])
def delete_bookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)
    db.session.delete(bookshelf)
    db.session.commit()

    return redirect(url_for('bookshelf.index'))


@bookshelf.route('/<int:bookshelf_id>')
def viewBookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)
    return render_template('viewBookshelf.html', bookshelf=bookshelf)


@bookshelf.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm(request.form)

    if request.method == 'POST' and form.validate():
        book = Book(name=form.name.data, description=form.description.data, author_id=1)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('bookshelf.index'))

    return render_template('add.html', form=form)

@bookshelf.route('/book/<book_id>')
def viewBook(book_id):
    book_id = Book.query.filter(Book.id == book_id).first_or_404()
    return render_template('single_book.html', book=book_id)

