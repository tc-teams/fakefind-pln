import os
from flask import Flask

def create_app():
    app = Flask(__name__)

   
    from .fakenews import pln as pln
    app.register_blueprint(pln)

    return app