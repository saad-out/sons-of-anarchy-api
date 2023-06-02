"""
The `character` module defines the `Character` class that represents a character in our Flask-SQLAlchemy API application.

The `Character` class inherits from `BaseModel` and defines attributes that are specific to characters such as `firstName`,
`lastName`, `age`, `gender`, and `club`.

Usage:
    To use this module, simply import the `Character` class and create instances of it:

    ```
    from api.v1.models.character import Character

    character = Character(
        firstName='John',
        lastName='Doe',
        gender='Male',
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

from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import Mapped


class Character(BaseModel, db.Model):
    """
    Represents a character in the TV show SOA.
    """
    __tablename__ = 'characters'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName: Mapped[str] = db.Column(db.String(64), nullable=False)
    middleName: Mapped[str] = db.Column(db.String(64))
    lastName: Mapped[str] = db.Column(db.String(64), nullable=False)
    fullName: Mapped[str] = db.Column(db.String(128), nullable=False)
    gender: Mapped[str] = db.Column(db.String(16), nullable=False)
    club: Mapped[str] = db.Column(db.String(64), nullable=False)
    occupation: Mapped[str] = db.Column(db.String(64), nullable=False)
    titles: Mapped[list[str]] = db.Column(db.JSON)
    aliases: Mapped[list[str]] = db.Column(db.JSON)
    playedBy: Mapped[list[str]] = db.Column(db.JSON, nullable=False)
    image: Mapped[str] = db.Column(db.String(64))

    def __repr__(self):
        return f'{self.fullName} ({self.gender}) - {self.club}'
    
    def to_dict(self):
        """
        Return a dictionary representation of the character instance.
        """
        IMAGE_URL_PREFIX = 'localhost:5000/api/v1/images/{image}'
        return {
            'id': self.id,
            'firstName': self.firstName,
            'middleName': self.middleName,
            'lastName': self.lastName,
            'fullName': self.fullName,
            'gender': self.gender,
            'club': self.club,
            'occupation': self.occupation,
            'titles': self.titles,
            'aliases': self.aliases,
            'playedBy': self.playedBy,
            'image': IMAGE_URL_PREFIX.format(image=self.image),
        }