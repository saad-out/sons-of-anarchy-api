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
from datetime import datetime

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


def create_season() -> Response:
    """
    """
    if not request.is_json:
        return make_response(jsonify({'message': 'Not a JSON'}), 400)

    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({'message': 'Not a JSON'}), 400)
    for column in ["seasonOrder", "title", "premierDate", "endDate", "synopsis"]:
        if column not in data:
            return make_response(jsonify({'message': f"Missing {column}"}), 400)

    try:
        data["premierDate"] = datetime.strptime(data["premierDate"], "%Y-%m-%d")
        data["endDate"] = datetime.strptime(data["endDate"], "%Y-%m-%d")
        season: Season = Season(**data)
        db.session.add(season)
        db.session.commit()
        return make_response(jsonify(season.to_dict()), 201)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Error occured!'}), 400)


def update_season(id: int) -> Response:
    """
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        return abort(404)
    if not request.is_json:
        return make_response(jsonify({'message': 'Not a JSON'}), 400)
    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({'message': 'Not a JSON'}), 400)

    season: Season = Season.query.filter_by(id=id).first()
    if not season:
        return abort(404)
    for key, value in data.items():
        if key in ["id", "createdAt", "updatedAt"]:
            continue
        if key in ["premierDate", "endDate"]:
            try:
                value = datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                continue
        setattr(season, key, value)
    db.session.commit()
    return make_response(jsonify(season.to_dict()), 200)


def delete_season(id: int) -> Response:
    """
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        return abort(404)

    season: Season = Season.query.filter_by(id=id).first()
    if not season:
        return abort(404)
    db.session.delete(season)
    db.session.commit()
    return make_response(jsonify({}), 200)