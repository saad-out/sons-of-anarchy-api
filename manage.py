from flask import Flask
from flask_migrate import Migrate
from src.api.v1.models import *
from src.api.v1.utils.database import db
from src.api.v1.utils.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/characters')
def characters():
    chars = db.session.query(Character).all()
    if chars:
        return chars[0].fullName
    else:
        return 'No characters found.'

if __name__ == '__main__':
    app.run(debug=True)
