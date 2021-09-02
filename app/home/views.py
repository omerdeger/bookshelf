from . import home

@home.route('/')
def home():
    return 'home'