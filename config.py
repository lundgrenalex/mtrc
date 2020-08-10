import logging
import logging.config
import os


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))


flask = {
    'host': '127.0.0.1',
    'port': '8087',
    'debug': True,
}

mrtc = {
    'exporter': {
        'basic_auth_security': {
            'enabled': False,
            'login': '',
            'password': '',
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
