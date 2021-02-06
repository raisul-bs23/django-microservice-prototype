from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/account/get-all-accounts')
def hello():
    response = [{"id": 1, "name": "John"}, {"id": 2, "name": "Doe"}]
    return jsonify(response)