"""
This module contains the routes for the images endpoints.
"""
from flask import Response

from api.v1.routes import app_routes
from api.v1.controllers.images import get_image


@app_routes.route('/images/<string:filename>', methods=['GET'])
def character_image(filename: str) -> Response:
    """
    Gets an image by filename.

    Args:
        filename (str): The filename of the image to get.

    Returns:
        A Flask Response object containing a JSON response
    """
    return get_image(filename)