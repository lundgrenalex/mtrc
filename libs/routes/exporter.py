import os
from flask import Blueprint, jsonify, request, Response
from libs.metric import export
import config

app = Blueprint('exporter', __name__, url_prefix='/metrics')


# Metrics page
@app.route('/', methods=['GET'])
def get_metrics():
    return Response(export.get_metrics(), mimetype='text'), 200
