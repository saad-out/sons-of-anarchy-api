"""
The `season` module defines the `Season` class for representing a season of a TV show.

The `Season` class is a subclass of `BaseModel` and inherits common fields such as `recordId`, `createdAt`, and `updatedAt`. It defines specific attributes that are unique to a season, such as the season order, title, premier and end dates, synopsis, and associated episodes.

Usage:
    To use this module, simply import the `Season` class and inherit it in your models:

    ```
    from api.v1.models.season import Season

    class MySeason(Season):
        __tablename__ = 'my_season_table'

        # define additional fields here
        ...
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


class Season(BaseModel, db.Model):
    """
    Represent a season of a TV show.

    Attributes:
        id (Mapped[int]): An integer column that uniquely identifies each season.
        seasonOrder (Mapped[str]): A string column that indicates the season order.
        title (Mapped[str]): A string column that represents the title of the season.
        premierDate (Mapped[datetime]): A timestamp column that indicates the premier date of the season.
        endDate (Mapped[datetime]): A timestamp column that indicates the end date of the season.
        synopsis (Mapped[str]): A text column that provides a synopsis of the season.
        episodes (Mapped[list[Episode]]): A relationship with the `Episode` class that represents the episodes associated with the season.

    Methods:
        __repr__(self): Return a string representation of the season instance.
    """
    __tablename__ = 'seasons'

    __table_args__ = (
        db.Index('ix_seasons_seasonOrder', 'seasonOrder'),
    )

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seasonOrder: Mapped[str] = db.Column(db.String(64), nullable=False, unique=True)
    title: Mapped[str] = db.Column(db.String(64), nullable=False)
    premierDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)
    endDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)
    synopsis: Mapped[str] = db.Column(db.Text, nullable=False)

    episodes: Mapped[list[Episode]] = db.relationship('Episode', backref='season', lazy=True)

    def __repr__(self):
        return f'Season {self.seasonOrder}: {self.title}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'seasonOrder': self.seasonOrder,
            'title': self.title,
            'premierDate': self.premierDate.strftime("%Y-%m-%d"),
            'endDate': self.endDate.strftime("%Y-%m-%d"),
            'synopsis': self.synopsis,
            'episodes': ["localhost:5000/api/v1/episodes/{}".format(episode.id)
                         for episode in self.episodes]
        }