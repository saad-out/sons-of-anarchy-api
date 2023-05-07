from api.v1.utils.database import db

from sqlalchemy.orm import Mapped
from datetime import datetime
import uuid

class BaseModel(db.Model):
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