# Lighthouse 100
# A simple flask server that scores 100 on all parts of the Lighthouse audit and is PWA optimised.
# Github: https://www.github.com/0x4248/lighthouse_100
# By: 0x4248

import flask
from flask import request, jsonify, send_from_directory
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    f = open("src/index.html", "r")
    return f.read()

@app.route('/robots.txt', methods=['GET'])
def robots():
    f = open("src/robots.txt", "r")
    return f.read()

@app.route('/manifest.json', methods=['GET'])
def manifest():
    f = open("src/manifest.json", "r")
    return f.read()

@app.route('/files/<path:path>', methods=['GET'])
def send_report(path):
    return send_from_directory('src', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443, ssl_context='adhoc')