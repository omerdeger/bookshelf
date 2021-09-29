from flask import render_template
from . import home
from ..models.bookshelf import Author


users = [
    {'name': 'Omer Deger', 'email': 'aysegul@to.co', 'password': 'password1', 'avatar':'omer.png'},
    {'name': 'Aysegul Deger', 'email': 'omer@to.co', 'password': 'password2', 'avatar':'aysegul.png'},
    {'name': 'Minnak Deger', 'email': 'minnak@to.co', 'password': 'password3', 'avatar':'baby.jpg'},
]

@home.route('/')
def index():
    return render_template('home.html', users=users, name="omer")