from flask import Blueprint
from flask import jsonify

example = Blueprint('example', __name__)


@example.route('/hello', methods=['GET'])
def hello():
    return jsonify({'Message': 'Hello world'}), 200
