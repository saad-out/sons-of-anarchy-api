"""
This module contains the routes for the episodes endpoints.
"""
from flask import jsonify, Response, request
from typing import Optional

from api.v1.routes import app_routes
from api.v1.utils.token import token_required
from api.v1.controllers.episodes import (
    get_episode_by_id,
    get_all_episodes,
    get_episode_for_season_by_id,
    get_episodes_for_season,
    create_episode,
    create_episode_for_season,
    update_episode,
    delete_episode
)


@app_routes.route('/episodes', methods=['GET'])
@app_routes.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episodes(episode_id: Optional[int] = None) -> Response:
    """
    Gets a list of all episodes or a single episode by ID.

    Args:
        episode_id (int, optional): The ID of the episode to get. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if episode_id:
        return get_episode_by_id(episode_id)
    else:
        return get_all_episodes()


@app_routes.route('/seasons/<int:season_id>/episodes', methods=['GET'])
@app_routes.route('/seasons/<int:season_id>/episodes/<int:episode_id>', methods=['GET'])
def get_season_episodes(season_id: int, episode_id: Optional[int] = None) -> Response:
    """
    Gets a list of all episodes for a season or a single episode by ID for a season.

    Args:
        season_id (int): The ID of the season to get episodes for.
        episode_id (int, optional): The ID of the episode to get. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if episode_id:
        return get_episode_for_season_by_id(season_id, episode_id)
    else:
        return get_episodes_for_season(season_id)


@app_routes.route('/episodes', methods=['POST'])
@app_routes.route('/episodes/<int:episode_id>', methods=['PUT', 'DELETE'])
@token_required
def post_episodes(episode_id: Optional[int] = None) -> Response:
    """
    Creates, updates, or deletes an episode.

    Args:
        episode_id (int, optional): The ID of the episode to modify. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if episode_id:
        if request.method == 'PUT':
            return update_episode(episode_id)
        else:
            return delete_episode(episode_id) 
    else:
        return create_episode()


@app_routes.route('/seasons/<int:season_id>/episodes', methods=['POST'])
@app_routes.route('/seasons/<int:season_id>/episodes/<int:episode_id>', methods=['PUT', 'DELETE'])
@token_required
def post_season_episodes(season_id: int, episode_id: Optional[int] = None) -> Response:
    """
    Creates, updates, or deletes an episode for a season.

    Args:
        season_id (int): The ID of the season to modify episodes for.
        episode_id (int, optional): The ID of the episode to modify. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if episode_id:
        if request.method == 'PUT':
            return update_episode(episode_id, season_id)
        else:
            return delete_episode(episode_id, season_id)
    else:
        return create_episode_for_season(season_id)