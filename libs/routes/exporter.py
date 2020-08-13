import os
from flask import Blueprint, jsonify, request, Response
from flask_httpauth import HTTPBasicAuth
from libs.metric import export
import config

app = Blueprint('exporter', __name__, url_prefix='/metrics')


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
    return Response(export.get_metrics(), mimetype='text'), 200
