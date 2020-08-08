import os
import glob
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
import prometheus_client
from libs.routes import create_app
import config


logging.basicConfig(
    format='%(asctime)-15s %(levelname)-8s %(name)-1s: %(message)s',
    level=logging.DEBUG,
)

# New start - clear DB
if config.prometheus['remove_database']:
    db_files = glob.glob('./tmp/*.db', recursive=True)
    for db_file in db_files:
        os.remove(db_file)


app = create_app()


if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(
        host=config.flask['host'],
        port=config.flask['port'],
        debug=config.flask['debug'])
