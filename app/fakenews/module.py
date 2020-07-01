from flask import Flask

app = Flask(__name__)

@app.route("/")
def pln():
    return "Hello, World!"