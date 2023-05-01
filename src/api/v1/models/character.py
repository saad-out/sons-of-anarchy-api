from api.v1.utils.database import db
from api.v1.models.base_model import BaseModel

from sqlalchemy.ext.mutable import MutableList


class Character(BaseModel, db.Model):
    """
    	id: Character ID, int
	firstName: Character's first name, str
	middleName: Character's middle name (optional), str
	lastName: Character's last name, str
	fullName: Character's full name, str
	age: Character's age, int
	gender: Character's gender, enum(str)
	club: Character's club, str
	occupation: Character's occupation (job), str
	titles: Character's titles, list of strs
	aliases: Character's nicknames, list of strs
	playedBy: Actor(s) who played the role, list of strss
    """
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
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
    