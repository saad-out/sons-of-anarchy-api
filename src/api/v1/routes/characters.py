from flask import request, jsonify, Response
from typing import Optional

from api.v1.routes import app_routes
from api.v1.utils.token import token_required


@app_routes.route('/characters', methods=['GET'])
@app_routes.route('/characters/<int:character_id>', methods=['GET'])
def get_characters(character_id: Optional[int] = None) -> Response:
    """
    """
    if character_id:
        return jsonify({'message': f'Get character {character_id}'})
    else:
        return jsonify({'message': 'Get all characters'})


@app_routes.route('/characters', methods=['POST'])
@app_routes.route('/characters/<int:character_id>', methods=['PUT', 'DELETE'])
@token_required
def post_characters(character_id: Optional[int] = None) -> Response:
    """
    """
    if character_id:
        if request.method == 'PUT':
            return jsonify({'message': f'Update character {character_id}'})
        else:
            return jsonify({'message': f'Delete character {character_id}'})
    else:
        return jsonify({'message': 'Create character'})