import os
from flask import Blueprint, jsonify, request, Response
import prometheus_client
from prometheus_client import multiprocess
import config

app = Blueprint('exporter', __name__, url_prefix='/metrics')

# Multiprocessing setup
# Cf. https://github.com/prometheus/client_python#multiprocess-mode-gunicorn
os.environ['prometheus_multiproc_dir'] = config.prometheus['db_pathname']
registry = prometheus_client.CollectorRegistry()
multiprocess.MultiProcessCollector(registry)


@app.route('/', methods=['GET'])
def get_metrics():
    return Response(
        prometheus_client.generate_latest(registry),
        mimetype=str('text/plain; version=0.0.4; charset=utf-8'))
