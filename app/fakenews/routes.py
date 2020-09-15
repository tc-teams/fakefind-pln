# -*- coding: utf-8 -*-
import sys 
import os
import json
import logging



from flask import request,Response

from . import pln,errors
sys.path.append(os.path.abspath("/code/natural-language-processing/bag-of-words"))
from compute_languages import *

LOG = logging.getLogger(__name__)


@pln.route("/", methods=['POST'])
def bag_of_words():
    req = json.loads(request.get_data().decode('utf-8'))
  
    if not bool(req):
        LOG.debug("Bad Request!")
        return handle_bad_request(400)
        
    description = req["description"]
    related = req["news"]
    result= {}

    for news in related :
        compare = cts_match(bow(description),bow(news))
        result[news] = compare
    

    data = json.dumps({
        "description": description,
        "pln-process":result,
    })

    LOG.info("Request completed :",data)

    return Response(data, status=200, mimetype='application/json')




@errors.errorhandler(400)
def handle_bad_request(e):
    return 'bad request!', 400





