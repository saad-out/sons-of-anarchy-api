"""
This __init__.py file initializes the Flask Blueprint 'app_routes' and sets up the URL prefix for the API version 1 endpoints.
It also imports and registers various routes related to characters, seasons, episodes, search, authentication, and images.

Attributes:
    app_routes (Blueprint): A Flask Blueprint object representing the API version 1 routes.

Usage:
    This file is intended to be imported and used within a Flask application to organize and register API routes for version 1.

Example:
    # Import and register the API version 1 routes
    from flask import Flask
    from api.v1 import app_routes

    app = Flask(__name__)
    app.register_blueprint(app_routes)

Note:
    The actual implementation of the routes is defined in the individual modules imported in this file.
"""
from flask import Blueprint

app_routes: Blueprint = Blueprint('app_routes', __name__, url_prefix='/api/v1')

from api.v1.routes.characters import *
from api.v1.routes.seasons import *
from api.v1.routes.episodes import *
# from api.v1.routes.search import *
from api.v1.routes.auth import *
from api.v1.routes.images import *