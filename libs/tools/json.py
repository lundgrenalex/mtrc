from functools import wraps
from flask import jsonify, request
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from werkzeug.exceptions import BadRequest
from importlib import import_module
import logging


def validate_schema(schema_name: str):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                schema = import_module('libs.schemas.' + schema_name, package=__name__)
                validate(request.json, schema.schema)
            except ValidationError as e:
                logging.error(f'ValidationError: {e.message}, {request.data}')
                return jsonify({
                    "error_code": 400,
                    "error_type": "ValidationError",
                    "error_message": e.message
                }), 400
            return f(*args, **kw)
        return wrapper
    return decorator
