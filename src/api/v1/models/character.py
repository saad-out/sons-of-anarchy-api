from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import Mapped


class Character(BaseModel, db.Model):
    __tablename__ = 'characters'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName: Mapped[str] = db.Column(db.String(64), nullable=False)
    middleName: Mapped[str] = db.Column(db.String(64))
    lastName: Mapped[str] = db.Column(db.String(64), nullable=False)
    fullName: Mapped[str] = db.Column(db.String(128), nullable=False)
    age: Mapped[int] = db.Column(db.Integer, nullable=False)
    gender: Mapped[str] = db.Column(db.String(16), nullable=False)
    club: Mapped[str] = db.Column(db.String(64), nullable=False)
    occupation: Mapped[str] = db.Column(db.String(64), nullable=False)
    titles: Mapped[list[str]] = db.Column(db.JSON)
    aliases: Mapped[list[str]] = db.Column(db.JSON)
    playedBy: Mapped[list[str]] = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'{self.fullName} ({self.age}) - {self.club}'