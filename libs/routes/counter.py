from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import counter

app = Blueprint('gateway-counter', __name__, url_prefix='/handler/counter')


@app.route('/', methods=['POST'])
@validate_schema('counter')
def get_counter():
    result = counter.update(request.json)
    return jsonify(result), 200


@app.route('/<string:metric_name>/', methods=['DELETE'])
def remove_metric(metric_name):
    result = counter.remove(metric_name)
    return jsonify(result), 200
