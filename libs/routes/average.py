from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import average

app = Blueprint('gateway-average', __name__, url_prefix='/handler/average')


@app.route('/', methods=['POST'])
@validate_schema('average')
def get_average():
    result = average.update(request.json)
    return jsonify(result), 200


@app.route('/<string:metric_name>/', methods=['DELETE'])
def remove_metric(metric_name):
    result = average.remove(metric_name)
    return jsonify(result), 200
