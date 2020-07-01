from flask import request
from . import pln

@pln.route("/", methods=['GET'])
def bag_of_words():
    #TODO implementar a chamada dos métodos de processamento de linguagem natural
    return "ola"




