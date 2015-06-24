from flask import Flask, request, redirect, jsonify

import json


app = Flask(__name__)

body = None

@app.route('/cards', methods=['GET'])
def retrieve_card_stack():
    global body
    if body is not None:
        return jsonify({
            'cards': [
                dict(body=body)
            ]
        })
    else:
        return jsonify({'cards':[]})

@app.route('/card', methods=['POST'])
def create_new_card():
    global body
    body = request.form['body']
    return redirect('/cards')
