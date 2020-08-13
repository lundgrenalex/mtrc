from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import counter, gauge

app = Blueprint('gateway-counter', __name__, url_prefix='/handler/counter')


@app.route('/', methods=['POST'])
@validate_schema('counter')
def get_counter():
    result = counter.update(request.json)
    return jsonify(result), 200
