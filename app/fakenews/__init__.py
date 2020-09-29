from flask import Blueprint


pln = Blueprint("pln", __name__)
pln_summary = Blueprint("pln_summary", __name__)
errors = Blueprint("errors", __name__)


from . import routes
