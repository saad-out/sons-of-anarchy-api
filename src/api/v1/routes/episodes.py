from flask import jsonify, Response
from typing import Optional

from api.v1.routes import app_routes


@app_routes.route('/episodes', methods=['GET'])
@app_routes.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episodes(episode_id: Optional[int] = None) -> Response:
    """
    """
    if episode_id:
        return jsonify({'message': f'Get episode {episode_id}'})
    else:
        return jsonify({'message': 'Get all episodes'})


@app_routes.route('/seasons/<int:season_id>/episodes', methods=['GET'])
@app_routes.route('/seasons/<int:season_id>/episodes/<int:episode_id>', methods=['GET'])
def get_season_episodes(season_id: int, episode_id: Optional[int] = None) -> Response:
    """
    """
    if episode_id:
        return jsonify({'message': f'Get season {season_id} episode {episode_id}'})
    else:
        return jsonify({'message': f'Get all season {season_id} episodes'})
