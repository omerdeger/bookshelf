from flask import render_template
from . import auth


@auth.route('/')
def index():
    return render_template('auth.html', title='Üye')

@auth.route('/login')
def sing_in():
    return render_template('login.html', title='Giriş')

@auth.route('/register')
def sing_up():
    return render_template('register.html', title='Kayıt')