from flask import Response

from api.v1.routes import app_routes
from api.v1.controllers.images import get_image


@app_routes.route('/images/<string:filename>', methods=['GET'])
def character_image(filename: str) -> Response:
    """
    """
    return get_image(filename)