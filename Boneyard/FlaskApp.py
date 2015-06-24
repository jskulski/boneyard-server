from flask import Flask

import json


app = Flask(__name__)


@app.route('/')
def homepage():
    return "lol"

@app.route('/card-stack')
def retrieve_card_stack():
    return json.dumps({})
