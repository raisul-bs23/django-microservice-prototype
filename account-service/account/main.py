from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/account/hello")
def hello():
    data = [
            {
                'id': 1,
                'name': 'Example Invoice 1'
            },
            {
                'id': 2,
                'name': 'Example Invoice 2'
            },

        ]

    response = {
            'data': data,
            'message': 'Response From Invoice Service',
        }
    return jsonify(response)