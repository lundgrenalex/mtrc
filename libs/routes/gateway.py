from flask import Blueprint, jsonify, request
from libs.tools.json import validate_schema
from libs.metric import counter, gauge

app = Blueprint('gateway', __name__, url_prefix='/handler')


@app.route('/counter', methods=['POST'])
@validate_schema('metric')
def get_counter():
    counter.update(request.json)
    return jsonify({'status': True}), 200


@app.route('/gauge', methods=['POST'])
@validate_schema('metric')
def get_gauge():
    gauge.update(request.json)
    return jsonify({'status': True}), 200
