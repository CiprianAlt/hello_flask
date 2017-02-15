from flask import Flask, json
from time import sleep
import logging
import os

app = Flask(__name__)
app.debug = True

stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)


@app.route('/')
@app.route('/delay=<int:delay>')
def root_url(delay=0):
    """ Just return hello world  """
    if delay > 0:
        sleep(delay)
    return 'Hello world!'

@app.route('/bacon')
def bacon_url(delay=0):
    """ Returns the place to buy the bacon """
    return 'Bankside Cafe, London, Southbank'

@app.route('/env/')
@app.route('/env')
@app.route('/hello_flask/env')
def env_url():
    """ Return all environment variables """
    return json.jsonify(os.environ.items())

@app.route('/ping/ping')
def ping():
    """ Return empty page """
    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # pragma: no cover
