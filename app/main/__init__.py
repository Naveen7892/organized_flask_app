from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes # putting this line above bp=... will cause circular import exception.

