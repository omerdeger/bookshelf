from flask import Blueprint

bookshelf = Blueprint('bookshelf', __name__, 
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='static/')

from . import views
