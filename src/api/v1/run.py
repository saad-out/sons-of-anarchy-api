"""
run.py: Flask API for the Sons of Anarchy TV show.

This module sets up a Flask application for a RESTful API related to the Sons of Anarchy TV show.
It initializes the necessary components, such as the database, routes, and error handlers.

The API provides endpoints for accessing and manipulating data related to the Sons of Anarchy TV show.

Usage:
    - Make sure the required dependencies are installed (Flask, Flask-Migrate, Flask-Cors, dotenv...).
    - Set the necessary environment variables in a .env file.
    - Run this module to start the Flask application.
"""
from flask import (
    Flask,
    jsonify,
    make_response,
    Response,
)
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from os import getenv

from api.v1.models import *
from api.v1.routes import app_routes
from api.v1.utils.database import db
from api.v1.utils.config import Config

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app: Flask = Flask(__name__)

# Configure Flask application
app.url_map.strict_slashes = False
app.config.from_object(Config)

# Database and migrations
db.init_app(app)
migrate: Migrate = Migrate(app, db)

# Enable CORS
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Register routes
app.register_blueprint(app_routes)


@app.errorhandler(404)
def not_found(error) -> Response:
    """
    Error handler for 404 Not Found errors.
    
    Args:
        error: The error that occurred.
    
    Returns:
        A Flask response containing a JSON object with an error message.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(405)
def method_not_allowed(error) -> Response:
    """
    Error handler for 405 Method Not Allowed errors.
    
    Args:
        error: The error that occurred.
    
    Returns:
        A Flask response containing a JSON object with an error message.
    """
    return make_response(jsonify({'error': 'Method not allowed'}), 405)


@app.errorhandler(500)
def internal_server_error(error) -> Response:
    """
    Error handler for 500 Internal Server Error errors.
    
    Args:
        error: The error that occurred.
    
    Returns:
        A Flask response containing a JSON object with an error message.
    """
    return make_response(jsonify({'error': 'Internal server error'}), 500)


if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(host=getenv('APP_HOST', '0.0.0.0'),
            port=int(getenv('APP_PORT', 5000)),
            debug=bool(getenv('DEBUG', False)))
