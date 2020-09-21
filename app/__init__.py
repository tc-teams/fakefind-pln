# Standard library imports
import os
import logging


# Third party imports
from flask import Flask

# Local application imports


def configure_logging():
    # register root logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)

def create_app():

    app = Flask(__name__)
    configure_logging()

    from .fakenews import pln, errors


    app.register_blueprint(pln)
    app.register_blueprint(errors)

    return app