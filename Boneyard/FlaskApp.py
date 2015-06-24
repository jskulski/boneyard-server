from flask import Flask, request, redirect, url_for

import json


app = Flask(__name__)

body = None

@app.route('/cards', methods=['GET'])
def retrieve_card_stack():
    global body
    if body is not None:
        return json.dumps(body)
    else:
        return json.dumps({})

@app.route('/card', methods=['POST'])
def create_new_card():
    global body
    body = request.form['body']
    return redirect('/cards')
