import sys 
import os
import json
import logging



from flask import request

from . import pln,errors

sys.path.append(os.path.abspath("/code/natural-language-processing/bag-of-words"))
from compute_languages import *

LOG = logging.getLogger(__name__)


@pln.route("/", methods=['POST'])
def bag_of_words():
    req = request.get_json()
  
    if not bool(req):
        LOG.debug("Bad Request!")
        return handle_bad_request(400)
        

    doc = req["news"]
    desc = req["description"]
    result= {}

    for d in doc:
        compare = cts_match(bow(desc),bow(d))
        result[d] = compare
    

    return result, 200


@errors.errorhandler(400)
def handle_bad_request(e):
    return 'bad request!', 400





