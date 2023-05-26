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
    