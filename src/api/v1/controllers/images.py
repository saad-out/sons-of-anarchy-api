from flask import (
    abort,
    Response,
    send_file
)


def get_image(filename: str) -> Response:
    """
    """
    try:
        return send_file(f'images/{filename}', mimetype='image/jpeg')
    except FileNotFoundError:
        return abort(404)