from flask import Blueprint

pln = Blueprint("pln", __name__)

from . import routes