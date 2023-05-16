from flask import jsonify, Response
from typing import Optional

from api.v1.routes import app_routes


@app_routes.route('/seasons', methods=['GET'])
@app_routes.route('/seasons/<int:season_id>', methods=['GET'])
def get_seasons(season_id: Optional[int] = None) -> Response:
    """
    """
    if season_id:
        return jsonify({'message': f'Get season {season_id}'})
    else:
        return jsonify({'message': 'Get all seasons'})
