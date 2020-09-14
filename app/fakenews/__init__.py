from flask import Blueprint


pln = Blueprint("pln", __name__)
errors = Blueprint("errors", __name__)


from . import routes