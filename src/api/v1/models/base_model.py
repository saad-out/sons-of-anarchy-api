from src.api.v1.utils.database import db

import uuid

class BaseModel(db.Model):
    """
    Attributes:
	recordId: Internal unique record ID, str
	createdAt: Record creation time, datetime
	updatedAT: Record update time, datetime
    """
    __abstract__ = True

    recordId = db.Column(db.String(36), primary_key=True)
    createdAt = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        self.recordId = str(uuid.uuid4())
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)