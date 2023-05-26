from flask import jsonify, Response, request
from typing import Optional

from api.v1.routes import app_routes
from api.v1.utils.token import token_required
from api.v1.controllers.episodes import (
    get_episode_by_id,
    get_all_episodes,
    get_episode_for_season_by_id,
    get_episodes_for_season
)


@app_routes.route('/episodes', methods=['GET'])
@app_routes.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episodes(episode_id: Optional[int] = None) -> Response:
    """
    """
    if episode_id:
        return get_episode_by_id(episode_id)
    else:
        return get_all_episodes()


@app_routes.route('/seasons/<int:season_id>/episodes', methods=['GET'])
@app_routes.route('/seasons/<int:season_id>/episodes/<int:episode_id>', methods=['GET'])
def get_season_episodes(season_id: int, episode_id: Optional[int] = None) -> Response:
    """
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
    """
    if episode_id:
        if request.method == 'PUT':
            return jsonify({'message': f'Update episode {episode_id}'})
        else:
            return jsonify({'message': f'Delete episode {episode_id}'})
    else:
        return jsonify({'message': 'Create episode'})


@app_routes.route('/seasons/<int:season_id>/episodes', methods=['POST'])
@app_routes.route('/seasons/<int:season_id>/episodes/<int:episode_id>', methods=['PUT', 'DELETE'])
@token_required
def post_season_episodes(season_id: int, episode_id: Optional[int] = None) -> Response:
    """
    """
    if episode_id:
        if request.method == 'PUT':
            return jsonify({'message': f'Update season {season_id} episode {episode_id}'})
        else:
            return jsonify({'message': f'Delete season {season_id} episode {episode_id}'})
    else:
        return jsonify({'message': f'Create season {season_id} episode'})