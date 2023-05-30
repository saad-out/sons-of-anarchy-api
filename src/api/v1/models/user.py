"""
The `user` module defines the `User` class that represents a user in our Flask-SQLAlchemy API application.

The `User` class inherits from `BaseModel` and defines attributes that are specific to users such as `firstName`,
`lastName`, `email`, and `password`.

Usage:
    To use this module, simply import the `User` class and create instances of it:

    ```
    from api.v1.models.user import User

    user = User(
        firstName='John',
        lastName='Doe',
        email='johndoe@mail.com',
        password='password',
    )
    ```

    Note: this module requires the `flask_sqlalchemy` and `sqlalchemy` packages to be installed.

References:
    - Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/
    - SQLAlchemy: https://www.sqlalchemy.org/
"""
from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.orm import Mapped


class User(BaseModel, db.Model):
    """
    Represents a user for the API application. 
    """
    __tablename__ = 'users'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName: Mapped[str] = db.Column(db.String(64), nullable=False)
    lastName: Mapped[str] = db.Column(db.String(64), nullable=False)
    email: Mapped[str] = db.Column(db.String(64), nullable=False, unique=True)
    password: Mapped[str] = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'{self.firstName} {self.lastName} ({self.email})'