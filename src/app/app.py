"""
This module is the main entry point for the Flask API application.

It is responsible for creating the Flask application and configuring it.
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    """
    This function is responsible for handling the /status endpoint.
    """
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    app.run(host=os.getenv("FLASK_HOST", "localhost"), port=os.getenv("FLASK_PORT", 5000), debug=True)