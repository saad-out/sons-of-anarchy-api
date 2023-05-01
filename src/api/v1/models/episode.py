from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel


class Episode(BaseModel, db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(64), nullable=False)
    episodeNumber = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    airDate = db.Column(db.DateTime, nullable=False)