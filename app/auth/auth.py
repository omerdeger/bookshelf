from . import auth


@auth.route('/login')
def login():
    return 'auth/login.html'