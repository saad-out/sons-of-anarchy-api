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
        age=35,
        gender='Male',
        club='Cool Club',
        occupation='Software Engineer',
        playedBy=['John Doe'],
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
    Define a `Character` class that represents a character in our Flask-SQLAlchemy API application.

    This class inherits from `BaseModel` and defines attributes that are specific to characters such as `firstName`,
    `lastName`, `age`, `gender`, and `club`.

    Attributes:
        id (Mapped[int]): An integer column that uniquely identifies each character.
        firstName (Mapped[str]): A string column that represents the character's first name.
        middleName (Mapped[str]): A string column that represents the character's middle name.
        lastName (Mapped[str]): A string column that represents the character's last name.
        fullName (Mapped[str]): A string column that represents the character's full name.
        age (Mapped[int]): An integer column that represents the character's age.
        gender (Mapped[str]): A string column that represents the character's gender.
        club (Mapped[str]): A string column that represents the character's club.
        occupation (Mapped[str]): A string column that represents the character's occupation.
        titles (Mapped[list[str]]): A JSON column that represents the character's titles.
        aliases (Mapped[list[str]]): A JSON column that represents the character's aliases.
        playedBy (Mapped[list[str]]): A JSON column that represents the actor(s) who played the character.

    Methods:
        __repr__(self): Return a string representation of the character instance.

    """
    __tablename__ = 'characters'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName: Mapped[str] = db.Column(db.String(64), nullable=False)
    middleName: Mapped[str] = db.Column(db.String(64))
    lastName: Mapped[str] = db.Column(db.String(64), nullable=False)
    fullName: Mapped[str] = db.Column(db.String(128), nullable=False)
    age: Mapped[int] = db.Column(db.Integer)
    gender: Mapped[str] = db.Column(db.String(16), nullable=False)
    club: Mapped[str] = db.Column(db.String(64), nullable=False)
    occupation: Mapped[str] = db.Column(db.String(64), nullable=False)
    titles: Mapped[list[str]] = db.Column(db.JSON)
    aliases: Mapped[list[str]] = db.Column(db.JSON)
    playedBy: Mapped[list[str]] = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'{self.fullName} ({self.age}) - {self.club}'
    
    def to_dict(self):
        """
        Return a dictionary representation of the character instance.
        """
        return {
            'id': self.id,
            'firstName': self.firstName,
            'middleName': self.middleName,
            'lastName': self.lastName,
            'fullName': self.fullName,
            'age': self.age,
            'gender': self.gender,
            'club': self.club,
            'occupation': self.occupation,
            'titles': self.titles,
            'aliases': self.aliases,
            'playedBy': self.playedBy,
        }