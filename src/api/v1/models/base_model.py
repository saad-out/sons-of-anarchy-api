"""
The `base_model` module defines a base model class that can be inherited by other models in our Flask-SQLAlchemy
API application.

The `BaseModel` class defines a set of common fields such as `recordId`, `createdAt`, and `updatedAt` that are
used across different models. By inheriting from this class, other models can avoid duplicating these fields
and associated logic.

Usage:
    To use this module, simply import the `BaseModel` class and inherit it in your models:

    ```
    from base_model import BaseModel

    class MyModel(BaseModel):
        __tablename__ = 'my_table'

        # define additional fields here
        ...
    ```

    Note: this module requires the `flask_sqlalchemy` and `sqlalchemy` packages to be installed.

References:
    - Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/
    - SQLAlchemy: https://www.sqlalchemy.org/
"""
from api.v1.utils.database import db

from sqlalchemy.orm import Mapped
from datetime import datetime
import uuid

class BaseModel(db.Model):
    """
    Define a base model for database tables with shared attributes.
    
    This class is an abstract class that defines shared attributes for all models in a database, such as a unique record ID, created and updated timestamps.

    Attributes:
        recordId (Mapped[str]): A string column that uniquely identifies each record.
        createdAt (Mapped[datetime]): A timestamp column that indicates when a record was created.
        updatedAt (Mapped[datetime]): A timestamp column that indicates when a record was last updated.

    Methods:
        __init__(self, *args: tuple, **kwargs: dict): Constructor method that sets the record ID and optional keyword arguments.
        __repr__(self): Return a string representation of the model instance.

    """
    __abstract__ = True

    recordId: Mapped[str] = db.Column(db.String(36), primary_key=True)
    createdAt: Mapped[datetime] = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updatedAt: Mapped[datetime] = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def __init__(self, *args: tuple, **kwargs: dict):
        self.recordId = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key != 'recordId':
                    setattr(self, key, value)

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.recordId)