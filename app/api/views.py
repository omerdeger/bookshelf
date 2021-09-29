from . import api as api

@api.route('/')
def index():
    return {'status': 'success'}