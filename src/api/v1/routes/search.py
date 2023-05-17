from flask import jsonify, Response, request
from typing import Optional

from api.v1.routes import app_routes


@app_routes.route('/search', methods=['GET'])
def search() -> Response:
    """
    """
    args = request.args
    args: Optional[dict] = dict(args)
    if len(args) != 2 or 'type' not in args:
        return jsonify({'message': 'Invalid search query'})
    return jsonify({'message': f'Search for {args}'})
