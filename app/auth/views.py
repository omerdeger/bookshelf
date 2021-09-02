from . import auth


@auth.route('/')
def index():
    return '''
    <a href="/">Home</a>
    '''