"""
This module contains the routes for the characters endpoints.
"""
from flask import (
    request,
    jsonify,
    Response
)
from typing import Optional

from api.v1.routes import app_routes
from api.v1.utils.token import token_required
from api.v1.controllers.characters import (
    get_character_by_id,
    get_all_characters,
    create_character,
    update_character,
    delete_character
)


@app_routes.route('/characters', methods=['GET'])
@app_routes.route('/characters/<int:character_id>', methods=['GET'])
def get_characters(character_id: Optional[int] = None) -> Response:
    """
    Gets a list of all characters or a single character by ID.

    Args:
        character_id (int, optional): The ID of the character to get. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if character_id:
        return get_character_by_id(character_id) 
    else:
        return get_all_characters()


@app_routes.route('/characters', methods=['POST'])
@app_routes.route('/characters/<int:character_id>', methods=['PUT', 'DELETE'])
@token_required
def modify_characters(character_id: Optional[int] = None) -> Response:
    """
    Creates, updates, or deletes a character.

    Args:
        character_id (int, optional): The ID of the character to modify. Defaults to None.

    Returns:
        A Flask Response object containing a JSON response
    """
    if character_id:
        if request.method == 'PUT':
            return update_character(character_id)
        else:
            return delete_character(character_id)
    else:
        return create_character()