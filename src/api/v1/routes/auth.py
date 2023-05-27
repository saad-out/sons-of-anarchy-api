from flask import request, jsonify, Response

from api.v1.routes import app_routes
from api.v1.controllers.auth import login_user


@app_routes.route('/login', methods=['POST'])
def login() -> Response:
    """
    """
    return login_user()