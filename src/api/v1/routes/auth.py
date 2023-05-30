"""
This module defines the routes for the API version 1 authentication endpoint.
"""
from flask import request, jsonify, Response

from api.v1.routes import app_routes
from api.v1.controllers.auth import login_user


@app_routes.route('/login', methods=['POST'])
def login() -> Response:
    """
    Authenticates a user and returns a JSON response
    containing the user's information and a JWT token.

    Returns:
        A Flask Response object containing a JSON response
    """
    return login_user()