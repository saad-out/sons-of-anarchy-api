"""
The `episode` module defines the `Episode` class, which represents a TV episode in our Flask-SQLAlchemy API application.

The `Episode` class inherits from the `BaseModel` class and defines a set of fields specific to TV episodes, such as `seasonNumber`, `episodeNumber`, `title`, `synopsis`, and `airDate`.

Usage:
    To use this module, simply import the `Episode` class and use it as follows:

    ```
    from episode import Episode

    episode = Episode(seasonNumber='1', episodeNumber=1, title='Pilot', synopsis='This is the first episode of the series', airDate=datetime(2020, 1, 1))
    ```

    Note: this module requires the `flask_sqlalchemy` and `sqlalchemy` packages to be installed.

References:
    - Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/
    - SQLAlchemy: https://www.sqlalchemy.org/
"""
from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.orm import Mapped
from datetime import datetime


class Episode(BaseModel, db.Model):
    """
    Represents a TV episode.

    This class defines fields specific to TV episodes, such as `seasonNumber`, `episodeNumber`, `title`, `synopsis`, and `airDate`.

    Attributes:
        id (Mapped[int]): A unique integer ID for the episode.
        seasonNumber (Mapped[str]): A string column that indicates the season number the episode belongs to.
        episodeNumber (Mapped[int]): An integer column that indicates the episode number within the season.
        title (Mapped[str]): A string column that indicates the title of the episode.
        synopsis (Mapped[str]): A text column that provides a summary of the episode's plot.
        airDate (Mapped[datetime]): A timestamp column that indicates the date the episode aired.

    Methods:
        __repr__(self): Return a string representation of the episode instance.

    """
    __tablename__ = 'episodes'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seasonNumber: Mapped[str] = db.Column(db.String(64), db.ForeignKey('seasons.seasonOrder'), nullable=False)
    episodeNumber: Mapped[int] = db.Column(db.Integer, nullable=False)
    title: Mapped[str] = db.Column(db.String(64), nullable=False)
    synopsis: Mapped[str] = db.Column(db.Text, nullable=False)
    airDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Episode {self.episodeNumber} from season {self.seasonNumber}'

    def to_dict(self):
        """
        Returns a dictionary representation of the episode instance.

        Returns:
            dict: A dictionary containing the episode's attributes.
        """
        return {
            'id': self.id,
            'seasonNumber': self.seasonNumber,
            'episodeNumber': self.episodeNumber,
            'title': self.title,
            'synopsis': self.synopsis,
            'airDate': self.airDate.strftime("%Y-%m-%d"),
            'season': "localhost:5000/api/v1/seasons/{}".format(self.season.id)
        }