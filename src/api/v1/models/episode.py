from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.orm import Mapped
from datetime import datetime


class Episode(BaseModel, db.Model):
    __tablename__ = 'episodes'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seasonNumber: Mapped[str] = db.Column(db.String(64), db.ForeignKey('seasons.seasonOrder'), nullable=False)
    episodeNumber: Mapped[int] = db.Column(db.Integer, nullable=False)
    title: Mapped[str] = db.Column(db.String(64), nullable=False)
    synopsis: Mapped[str] = db.Column(db.Text, nullable=False)
    airDate: Mapped[datetime] = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Episode {self.episodeNumber} from season {self.seasonNumber}'