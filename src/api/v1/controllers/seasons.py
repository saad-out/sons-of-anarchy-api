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

from api.v1.models.season import Season
from api.v1.utils.database import db


def get_season_by_id(id: int) -> Response:
    """
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        abort(404)

    season: Season = Season.query.filter_by(id=id).first()
    if not season:
        abort(404)
    return make_response(jsonify(season.to_dict()), 200)


def get_all_seasons() -> Response:
    """
    """
    query = db.session.query(Season)
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
    seasons: List[Dict] = [season.to_dict() for season in query.all()]
    return make_response(jsonify(seasons), 200)