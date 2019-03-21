from flask import Blueprint
from flask import jsonify

example = Blueprint('example', __name__)

# GET is the default method, no need to declare it!
@example.route('/hello')
def hello():
    return jsonify({'Message': 'Hello world!'}), 200
