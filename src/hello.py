# hello.py
from flask import Flask, make_response

app = Flask(__name__)

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