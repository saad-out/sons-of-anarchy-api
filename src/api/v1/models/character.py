from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.ext.mutable import MutableList


class Character(BaseModel, db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(64), nullable=False)
    middleName = db.Column(db.String(64))
    lastName = db.Column(db.String(64), nullable=False)
    fullName = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(16), nullable=False)
    club = db.Column(db.String(64), nullable=False)
    occupation = db.Column(db.String(64), nullable=False)
    titles = MutableList.as_mutable(db.ARRAY(db.String(64)))
    aliases = MutableList.as_mutable(db.ARRAY(db.String(64)))
    playedBy = MutableList.as_mutable(db.ARRAY(db.String(64)))
    
    def __repr__(self):
        return f'{self.fullName} ({self.age}) - {self.club}'