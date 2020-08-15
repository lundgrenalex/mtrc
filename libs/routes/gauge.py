from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import gauge

app = Blueprint('gateway-gauge', __name__, url_prefix='/handler/gauge')


@app.route('/', methods=['POST'])
@validate_schema('gauge')
def get_gauge():
    result = gauge.update(request.json)
    return jsonify(result), 200


@app.route('/<string:metric_name>/', methods=['DELETE'])
def remove_metric(metric_name):
    result = gauge.remove(metric_name)
    return jsonify(result), 200
