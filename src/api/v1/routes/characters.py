from flask import request, jsonify, Response
from typing import Optional

from api.v1.routes import app_routes
from api.v1.utils.token import token_required
from api.v1.controllers.characters import (
    get_character_by_id,
    get_all_characters,
    create_character,
    update_character
)


@app_routes.route('/characters', methods=['GET'])
@app_routes.route('/characters/<int:character_id>', methods=['GET'])
def get_characters(character_id: Optional[int] = None) -> Response:
    """
    """
    if character_id:
        return get_character_by_id(character_id) 
    else:
        return get_all_characters()


@app_routes.route('/characters', methods=['POST'])
@app_routes.route('/characters/<int:character_id>', methods=['PUT', 'DELETE'])
@token_required
def post_characters(character_id: Optional[int] = None) -> Response:
    """
    """
    if character_id:
        if request.method == 'PUT':
            return update_character(character_id)
        else:
            return jsonify({'message': f'Delete character {character_id}'})
    else:
        return create_character()