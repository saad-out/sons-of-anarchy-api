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
from sqlalchemy.exc import IntegrityError


from api.v1.models.episode import Episode
from api.v1.models.season import Season
from api.v1.utils.database import db


def get_episode_by_id(id: int) -> Response:
    """
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        abort(404)

    episode: Episode = Episode.query.filter_by(id=id).first()
    if not episode:
        abort(404)
    return make_response(jsonify(episode.to_dict()), 200)


def get_all_episodes() -> Response:
    """
    """
    query = db.session.query(Episode)
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
    episodes: List[Dict] = [episode.to_dict() for episode in query.all()]
    return make_response(jsonify(episodes), 200)


def get_episode_for_season_by_id(season_id: int, episode_id: int) -> Response:
    """
    """
    try:
        assert type(season_id) == type(episode_id) == int
        assert season_id > 0 and episode_id > 0
    except AssertionError:
        abort(404)

    episode: Episode = Episode.query.filter_by(id=episode_id).first()
    if not episode:
        abort(404)
    season: Season = Season.query.filter_by(id=season_id).first()
    if (not season) or (episode not in season.episodes):
        abort(404)
    return make_response(jsonify(episode.to_dict()), 200)


def get_episodes_for_season(season_id: int) -> Response:
    """
    """
    try:
        assert type(season_id) == int and season_id > 0
    except AssertionError:
        abort(404)
    season: Season = Season.query.filter_by(id=season_id).first()
    if not season:
        abort(404)
    episodes: List[Dict] = [episode.to_dict() for episode in season.episodes]
    return make_response(jsonify(episodes), 200)


def create_episode() -> Response:
    """
    """    
    if not request.is_json:
        return make_response(jsonify({"message": "Not a JSON"}), 400)

    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({"message": "Not a JSON"}), 400)
    for column in ["seasonNumber", "episodeNumber", "title", "synopsis", "airDate"]:
        if column not in data:
            return make_response(jsonify({"message": f"Missing {column}"}), 400)

    try:
        episode: Episode = Episode(**data)
        db.session.add(episode)
        db.session.commit()
        return make_response(jsonify(episode.to_dict()), 201)
    except IntegrityError:
        return make_response(jsonify({"message": "Invalid data"}), 400)
    except Exception:
        return make_response(jsonify({"message": "Error occured!"}), 400)


def create_episode_for_season(id: int) -> Response:
    """
    """
    try:
        assert type(id) == int and id > 0
    except AssertionError:
        abort(404)
    if not request.is_json:
        return make_response(jsonify({"message": "Not a JSON"}), 400)
    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({"message": "Not a JSON"}), 400)
    for column in ["episodeNumber", "title", "synopsis", "airDate"]:
        if column not in data:
            return make_response(jsonify({"message": f"Missing {column}"}), 400)

    try:
        season: Season = Season.query.filter_by(id=id).first()
        if not season:
            abort(404)
        data["seasonNumber"] = season.seasonOrder
        episode: Episode = Episode(**data)
        db.session.add(episode)
        db.session.commit()
        return make_response(jsonify(episode.to_dict()), 201)
    except Exception:
        return make_response(jsonify({"message": "Error occured!"}), 400)


def update_episode(episode_id: int, season_id: Optional[int] = None) -> Response:
    """
    """
    season: Optional[Season] = None
    if season_id:
        try:
            assert type(season_id) == int and season_id > 0
        except AssertionError:
            abort(404)
        season = Season.query.filter_by(id=season_id).first()
        if not season:
            abort(404)
        
    if not request.is_json:
        return make_response(jsonify({"message": "Not a JSON"}), 400)
    try:
        data: Dict = request.get_json()
    except Exception:
        return make_response(jsonify({"message": "Not a JSON"}), 400)

    episode: Episode = Episode.query.filter_by(id=episode_id).first()
    if (not episode) or (season and episode not in season.episodes):
        abort(404)
    for key, value in data.items():
        if key in ["id", "createdAt", "updatedAt"]:
            continue
        if key == "airDate":
            try:
                value = datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                continue
        setattr(episode, key, value)
    if season_id and season:
        episode.seasonNumber = season.seasonOrder
    try:
        db.session.commit()
        return make_response(jsonify(episode.to_dict()), 200)
    except IntegrityError:
        return make_response(jsonify({"message": "Invalid data"}), 400)
    except Exception:
        return make_response(jsonify({"message": "Error occured!"}), 400)


def delete_episode(episode_id: int, season_id: Optional[int] = None) -> Response:
    """
    """
    season: Optional[Season] = None
    try:
        assert type(episode_id) == int and episode_id > 0
    except AssertionError:
        abort(404)
    if season_id:
        try:
            assert type(season_id) == int and season_id > 0
        except AssertionError:
            abort(404)
        season = Season.query.filter_by(id=season_id).first()
        if not season:
            abort(404)

    episode: Episode = Episode.query.filter_by(id=episode_id).first()
    if (not episode) or (season and episode not in season.episodes):
        abort(404)
    try:
        db.session.delete(episode)
        db.session.commit()
        return make_response(jsonify({}), 200)
    except Exception:
        return make_response(jsonify({"message": "Error occured!"}), 400)