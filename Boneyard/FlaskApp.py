from flask import Flask, request, redirect, jsonify, url_for

app = Flask(__name__)

body = None

@app.route('/cards', methods=['GET'])
def retrieve_card_list():
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
    if request.method == 'GET':
        print 'GET'
        return 'GET?!'
    global body
    body = request.form['body']
    return redirect(url_for('retrieve_card_list'))

if __name__ == "__main__":
    app.debug = True
    app.run()
