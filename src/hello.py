# hello.py
from flask import Flask, make_response
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return 'Hello, Batot!'

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response

if __name__ == '__main__':
    app.run()