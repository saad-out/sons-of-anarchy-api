from flask import jsonify, Response, request
from typing import Optional

from api.v1.routes import app_routes
from api.v1.utils.token import token_required
from api.v1.controllers.seasons import (
    get_season_by_id,
    get_all_seasons,
    create_season,
    update_season,
    delete_season
)


@app_routes.route('/seasons', methods=['GET'])
@app_routes.route('/seasons/<int:season_id>', methods=['GET'])
def get_seasons(season_id: Optional[int] = None) -> Response:
    """
    """
    if season_id:
        return get_season_by_id(season_id)
    else:
        return get_all_seasons()


@app_routes.route('/seasons', methods=['POST'])
@app_routes.route('/seasons/<int:season_id>', methods=['PUT', 'DELETE'])
@token_required
def post_seasons(season_id: Optional[int] = None) -> Response:
    """
    """
    if season_id:
        if request.method == 'PUT':
            return update_season(season_id)
        else:
            return delete_season(season_id)
    else:
        return create_season()