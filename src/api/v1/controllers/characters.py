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