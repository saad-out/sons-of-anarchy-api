"""
This module contains the controllers for the characters endpoints.
"""
from flask import (
    abort,
    jsonify,
    request,
    Response,
    make_response
)
from typing import (
    Optional,
    List,
    Dict
)

from api.v1.utils.database import db
from api.v1.models.character import Character


def get_character_by_id(id: int) -> Response:
    """
    Gets a character by ID.

    Args:
        id (int): The ID of the character to get.

    Returns:
        A Flask Response object containing a JSON response
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        return abort(404)

    character: Character = Character.query.filter_by(id=id).first()
    if not character:
        return abort(404)
    return make_response(jsonify(character.to_dict()), 200)


def get_all_characters() -> Response:
    """
    Gets a list of all characters.

    Returns:
        A Flask Response object containing a JSON response
    """
    query = db.session.query(Character)
    limit: Optional[str] = request.args.get("limit")
    if limit:
        try:
            query = query.limit(int(limit))
        except ValueError:
            pass
    offset: Optional[str] = request.args.get("offset")
    if offset:
        try:
            query = query.offset(int(offset)) 
        except ValueError:
            pass

    characters: List[Dict] = [character.to_dict() for character in query.all()]
    return make_response(jsonify(characters), 200)


def create_character() -> Response:
    """
    Creates a character.

    Returns:
        A Flask Response object containing a JSON response
    """
    if not request.is_json:
        return make_response(jsonify({"message": "Not a JSON"}), 400)

    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({"message": "Not a JSON"}), 400)
    for column in ["firstName", "lastName", "fullName","gender",
                   "club", "occupation", "playedBy"]:
        if column not in data:
            return make_response(jsonify({"message": f"Missing {column}"}), 400)

    try:
        character: Character = Character(**data)
        db.session.add(character)
        db.session.commit()
        return make_response(jsonify(character.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"message": "Error occured!"}), 400)


def update_character(id: int) -> Response:
    """
    Updates a character.

    Args:
        id (int): The ID of the character to update.

    Returns:
        A Flask Response object containing a JSON response
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        return abort(404)
    if not request.is_json:
        return make_response(jsonify({"message": "Not a JSON"}), 400)
    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({"message": "Not a JSON"}), 400)

    character: Character = Character.query.filter_by(id=id).first()
    if not character:
        return abort(404)
    for key, value in data.items():
        if key not in ["id", "createdAt", "updatedAt"]:
            setattr(character, key, value)
    db.session.commit()
    return make_response(jsonify(character.to_dict()), 200)


def delete_character(id: int) -> Response:
    """
    Deletes a character.

    Args:
        id (int): The ID of the character to delete.

    Returns:
        A Flask Response object containing a JSON response
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        return abort(404)

    character: Character = Character.query.filter_by(id=id).first()
    if not character:
        return abort(404)
    db.session.delete(character)
    db.session.commit()
    return make_response(jsonify({}), 200)