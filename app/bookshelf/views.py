from . import bookshelf


@bookshelf.route('/')
def index():
    return '''
    <a href="/">Home</a>
    '''