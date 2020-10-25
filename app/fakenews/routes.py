from flask import request
from . import pln

from npl.compute_languages import cts_match, bow

@pln.route("/", methods=['POST'])
def bag_of_words():
    document = request.args.get("document")

    limilarity = cts_match(bow(document),bow(document))

    return limilarity, 200




