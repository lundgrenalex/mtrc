import logging
import logging.config
from werkzeug.security import generate_password_hash
import os


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))


flask = {
    'host': '127.0.0.1',
    'port': '8087',
    'debug': True,
    'sentry_dsn': None,
}

mrtc = {
    'exporter': {
        'basic_auth_security': {
            'disabled': True,
            'users': {
                'user1': generate_password_hash(''),
            }
        },
    }
}

prometheus = {
    'db_pathname': './tmp',
    'remove_database': True,
}

# Overwrite config by your local
try:
    from configs.local import *  # noqa
except ImportError:
    pass
