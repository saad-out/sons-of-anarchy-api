"""
Season:
******
Attributes:
	id: Season ID, int
	seasonOrder: The season number, str
	title: Season's title, str
	premierDate: Air date, datetime
	endDate: Finale date, datetime
	synopsis: Season summary, str(Text)
	episodes: Season episodes, list 
"""
from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.ext.mutable import MutableList


class Season(BaseModel, db.Model):
    __tablename__ = 'seasons'

    id = db.Column(db.Integer, primary_key=True)
    seasonOrder = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    premierDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    episodes = MutableList.as_mutable(db.ARRAY(db.String(64)))