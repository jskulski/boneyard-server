from flask import Flask

import json


app = Flask(__name__)

@app.route('/cards', methods=['GET'])
def retrieve_card_stack():
    return json.dumps({})

@app.route('/card', methods=['POST'])
def create_new_card():
    return 'hello!'
