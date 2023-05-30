"""
This module contains the controllers for the images endpoints.
"""
from flask import (
    abort,
    Response,
    send_file
)


def get_image(filename: str) -> Response:
    """
    Gets an image by filename.

    Args:
        filename (str): The filename of the image to get.

    Returns:
        A Flask Response object containing a file, or a 404 if the file is not found
    """
    try:
        return send_file(f'images/{filename}', mimetype='image/jpeg')
    except FileNotFoundError:
        return abort(404)