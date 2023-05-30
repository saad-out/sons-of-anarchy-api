"""
The `base_model` module defines a base model class that can be inherited by other models in our Flask-SQLAlchemy
API application.

The `BaseModel` class defines a set of common fields such as `recordId`, `createdAt`, and `updatedAt` that are
used across different models. By inheriting from this class, other models can avoid duplicating these fields
and associated logic.
"""
from api.v1.utils.database import db

from sqlalchemy.orm import Mapped
from datetime import datetime
import uuid

class BaseModel(db.Model):
    """
    Define a base model for database tables with shared attributes.
    
    This class is an abstract class that defines shared attributes for all models in a database, such as a unique record ID, created and updated timestamps.
    """
    __abstract__ = True

    recordId: Mapped[str] = db.Column(db.String(36), primary_key=True)
    createdAt: Mapped[datetime] = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updatedAt: Mapped[datetime] = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, *args: tuple, **kwargs: dict):
        """
        Constructor method that sets the record ID and optional keyword arguments.

        Args:
            *args (tuple): Variable length argument list.
            **kwargs (dict): Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if 'recordId' not in kwargs:
                self.recordId = str(uuid.uuid4())
            if 'createdAt' not in kwargs:
                self.createdAt = datetime.utcnow()
            if 'updatedAt' not in kwargs:
                self.updatedAt = self.createdAt 
        else:
            self.recordId = str(uuid.uuid4())
            self.createdAt = datetime.utcnow()
            self.updatedAt = self.createdAt
        

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.recordId)