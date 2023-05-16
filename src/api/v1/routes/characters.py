from flask import request, jsonify, Response
from typing import Optional

from api.v1.routes import app_routes


@app_routes.route('/characters', methods=['GET'])
@app_routes.route('/characters/<int:character_id>', methods=['GET'])
def get_characters(character_id: Optional[int] = None) -> Response:
    """
    """
    if character_id:
        return jsonify({'message': f'Get character {character_id}'})
    else:
        return jsonify({'message': 'Get all characters'})
