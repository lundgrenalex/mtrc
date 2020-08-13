import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from libs.routes import create_app
import config


logging.basicConfig(
    format='%(asctime)-15s %(levelname)-8s %(name)-1s: %(message)s',
    level=logging.DEBUG,
    filename='./logs/mrtc.log',
)


app = create_app()


if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(
        host=config.flask['host'],
        port=config.flask['port'],
        debug=config.flask['debug'])
