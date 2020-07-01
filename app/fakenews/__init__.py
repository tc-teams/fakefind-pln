from flask import Blueprint

pln = Blueprint("pln", __name__)

def configure(app):
    app.register_blueprint(pln)

from . import routes