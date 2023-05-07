from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel
from api.v1.models.episode import Episode

from sqlalchemy.orm import Mapped
from datetime import datetime


class Season(BaseModel, db.Model):
    __tablename__ = 'seasons'

    __table_args__ = (
        db.Index('ix_seasons_seasonOrder', 'seasonOrder'),
    )

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seasonOrder: Mapped[str] = db.Column(db.String(64), nullable=False, unique=True)
    title: Mapped[str] = db.Column(db.String(64), nullable=False)
    premierDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)
    endDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)
    synopsis: Mapped[str] = db.Column(db.Text, nullable=False)

    episodes: Mapped[list[Episode]] = db.relationship('Episode', backref='season', lazy=True)

    def __repr__(self):
        return f'Season {self.seasonOrder}: {self.title}'