"""
This module contains the routes for the seasons endpoints.
"""
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
    Gets a list of all seasons or a single season by ID.

    Args:
        season_id (int, optional): The ID of the season to get. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if season_id:
        return get_season_by_id(season_id)
    else:
        return get_all_seasons()


@app_routes.route('/seasons', methods=['POST'])
@app_routes.route('/seasons/<int:season_id>', methods=['PUT', 'DELETE'])
@token_required
def modify_seasons(season_id: Optional[int] = None) -> Response:
    """
    Creates, updates, or deletes a season.

    Args:
        season_id (int, optional): The ID of the season to modify. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if season_id:
        if request.method == 'PUT':
            return update_season(season_id)
        else:
            return delete_season(season_id)
    else:
        return create_season()