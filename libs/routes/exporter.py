import os
from flask import Blueprint, jsonify, request, Response
from flask_httpauth import HTTPBasicAuth
import prometheus_client
from prometheus_client import multiprocess
import config

app = Blueprint('exporter', __name__, url_prefix='/metrics')

# Multiprocessing setup
# Cf. https://github.com/prometheus/client_python#multiprocess-mode-gunicorn
os.environ['prometheus_multiproc_dir'] = config.prometheus['db_pathname']
registry = prometheus_client.CollectorRegistry()
multiprocess.MultiProcessCollector(registry)


# Security optional
auth = HTTPBasicAuth()
@auth.verify_password
def verify_password(username, password):
    users = config.mrtc['exporter']['basic_auth_security']['users']
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

# Metrics page
@app.route('/', methods=['GET'])
@auth.login_required(
    optional=config.mrtc['exporter']['basic_auth_security']['disabled'])
def get_metrics():
    return Response(
        prometheus_client.generate_latest(registry),
        mimetype=str('text/plain; version=0.0.4; charset=utf-8'))
