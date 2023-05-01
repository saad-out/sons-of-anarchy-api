from api.v1.utils.database import db

import uuid

class BaseModel(db.Model):
    __abstract__ = True

    recordId = db.Column(db.String(36), primary_key=True)
    createdAt = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        self.recordId = str(uuid.uuid4())
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)