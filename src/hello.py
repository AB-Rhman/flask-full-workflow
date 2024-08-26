from flask import Flask, make_response
from prometheus_flask_exporter import PrometheusMetrics
import logging
import sys

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logger = logging.getLogger('flask-app')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def hello():
    logger.info('Hello endpoint was accessed')
    return 'Hello, Batot!'

@app.route('/<page_name>')
def other_page(page_name):
    logger.warning(f"Attempted to access non-existent page: {page_name}")
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response

if __name__ == '__main__':
    app.run()