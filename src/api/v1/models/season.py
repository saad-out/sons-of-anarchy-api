from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel


class Season(BaseModel, db.Model):
    __tablename__ = 'seasons'

    __table_args__ = (
        db.Index('ix_seasons_seasonOrder', 'seasonOrder'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seasonOrder = db.Column(db.String(64), nullable=False, unique=True)
    title = db.Column(db.String(64), nullable=False)
    premierDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    synopsis = db.Column(db.Text, nullable=False)

    episodes = db.relationship('Episode', backref='season', lazy=True)

    def __repr__(self):
        return f'Season {self.seasonOrder}: {self.title}'