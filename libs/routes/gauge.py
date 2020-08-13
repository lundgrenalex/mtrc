from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import counter, gauge

app = Blueprint('gateway', __name__, url_prefix='/handler/gauge')


@app.route('/', methods=['POST'])
@validate_schema('gauge')
def get_gauge():
    result = gauge.update(request.json)
    return jsonify(result), 200
