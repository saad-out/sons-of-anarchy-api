"""
The `season` module defines the `Season` class for representing a season of a TV show.

The `Season` class is a subclass of `BaseModel` and inherits common fields such as `recordId`, `createdAt`, and `updatedAt`. It defines specific attributes that are unique to a season, such as the season order, title, premier and end dates, synopsis, and associated episodes.

Usage:
    To use this module, simply import the `Season` class and inherit it in your models:

    ```
    from api.v1.models.season import Season

    season = Season(
        seasonOrder='S01',
        title='Season 1',
        ...
    )
    ```

    Note: this module requires the `flask_sqlalchemy` and `sqlalchemy` packages to be installed.

References:
    - Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/
    - SQLAlchemy: https://www.sqlalchemy.org/
"""
from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel
from api.v1.models.episode import Episode

from sqlalchemy.orm import Mapped
from datetime import datetime
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Season(BaseModel, db.Model):
    """
    Represent a season of a TV show.
    """
    __tablename__ = 'seasons'

    APP_URL = getenv('APP_URL', 'http://localhost:5000')

    __table_args__ = (
        db.Index('ix_seasons_seasonOrder', 'seasonOrder'),
    )

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seasonOrder: Mapped[str] = db.Column(db.String(64), nullable=False, unique=True)
    premierDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)
    endDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)
    synopsis: Mapped[str] = db.Column(db.Text, nullable=False)
    numberOfEpisodes: Mapped[int] = db.Column(db.Integer, nullable=False)
    viewership: Mapped[int] = db.Column(db.Float(precision=2), nullable=False)

    episodes: Mapped[list[Episode]] = db.relationship('Episode', backref='season', lazy=True)

    def __repr__(self):
        return f'Season {self.seasonOrder}: {self.title}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'seasonOrder': self.seasonOrder,
            'premierDate': self.premierDate.strftime("%Y-%m-%d"),
            'endDate': self.endDate.strftime("%Y-%m-%d"),
            'synopsis': self.synopsis,
            'numberOfEpisodes': self.numberOfEpisodes,
            'viewership': self.viewership,
            'episodes': ["{}/api/v1/episodes/{}".format(self.APP_URL, episode.id)
                         for episode in self.episodes]
        }