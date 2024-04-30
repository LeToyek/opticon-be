from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

