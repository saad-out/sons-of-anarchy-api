"""
This module contains controllers for the `/filter` endpoint.
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
    Dict,
    Tuple
)

from api.v1.utils.database import db
from api.v1.models.character import Character
from api.v1.models.season import Season
from api.v1.models.episode import Episode


TYPES: Dict = {"characters": Character, "seasons": Season, "episodes": Episode}
BASE_COLUMNS: Tuple = ("recordId", "createdAt", "updatedAt")
REQUIRED_FIELDS: Tuple = ("type", "filters")
ARRAY_COLUMNS: Tuple = ("writtenBy", "directedBy",
                        "playedBy","titles", "aliases")


def filter_type_by_attributes() -> Response:
    """
    Filters a type by attributes.

    Returns:
        A Flask Response object containing a JSON response
    """
    try:
        assert request.is_json
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for field in REQUIRED_FIELDS:
        if field not in data:
            return make_response(jsonify({"error": f"Missing field: {field}"}), 400)
    if data["type"] not in TYPES:
        return make_response(jsonify({"error": "Invalid type"}), 400)
    if not isinstance(data["filters"], dict):
        return make_response(jsonify({"error": "Invalid filters"}), 400)

    query = db.session.query(TYPES[data["type"]])
    for column, value in data["filters"].items():
        if column not in TYPES[data["type"]].__table__.columns:
            return make_response(jsonify({"error": "Invalid filters"}), 400)
        if column in BASE_COLUMNS:
            continue
        if column in ARRAY_COLUMNS and not isinstance(value, list):
            query = query.filter(getattr(TYPES[data["type"]], column).any(value))
            continue
        query = query.filter_by(**{column: value})

    return make_response(jsonify([record.to_dict() for record in query.all()]), 200)