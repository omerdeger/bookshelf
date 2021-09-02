from flask import Blueprint

bookshelf = Blueprint('bookshelf', __name__)

from . import views
