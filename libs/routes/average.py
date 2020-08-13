from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import average

app = Blueprint('gateway-average', __name__, url_prefix='/handler/average')


@app.route('/', methods=['POST'])
@validate_schema('average')
def get_average():
    result = average.update(request.json)
    return jsonify(result), 200
