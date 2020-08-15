import os
from flask import Blueprint, jsonify, request, Response
from libs.metric import exporter
import config

app = Blueprint('exporter', __name__, url_prefix='/metrics')


# Metrics page
@app.route('/', methods=['GET'])
def get_metrics():
    return Response(exporter.get_metrics(), mimetype='text'), 200


@app.route('/', methods=['DELETE'])
def drop_metrics():
    exporter.drop_all_metrics()
    return {}, 200
