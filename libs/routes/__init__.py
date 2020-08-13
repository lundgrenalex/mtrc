from flask import Flask, jsonify, g
from libs.tools.encoders import FlaskEncoder
import sentry_sdk
import config
from sentry_sdk.integrations.flask import FlaskIntegration
# incoming primitives
from .counter import app as counter_app
from .gauge import app as gauge_app
from .average import app as average_app
# exporter
from .exporter import app as exporter_app


def not_found(e):
    return jsonify({
        'error_code': 404,
        'error_message': 'Not Found'
    }), 404


def server_error(e):
    return jsonify({
        'error_code': 500,
        'error_message': 'Server Error'
    }), 500


def create_app():
    sentry_sdk.init(
        dsn=config.flask['sentry_dsn'], integrations=[FlaskIntegration()])
    app = Flask(__name__)
    app.register_blueprint(counter_app)
    app.register_blueprint(gauge_app)
    app.register_blueprint(average_app)
    app.register_blueprint(exporter_app)
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)
    app.json_encoder = FlaskEncoder
    return app
