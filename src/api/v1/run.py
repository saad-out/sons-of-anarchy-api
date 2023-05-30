from flask import (
    Flask,
    jsonify,
    make_response,
    Response,
)
from flask_migrate import Migrate
from flask_cors import CORS

from api.v1.models import *
from api.v1.routes import app_routes
from api.v1.utils.database import db
from api.v1.utils.config import Config

app: Flask = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
db.init_app(app)
migrate: Migrate = Migrate(app, db)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app.register_blueprint(app_routes)


@app.route('/')
def index() -> str:
    return 'Hello, World! and Welcome to the Sons Of Anarchy API version 1 !'

@app.route('/characters')
def characters() -> str:
    chars: list[Character] = db.session.query(Character).all()
    if chars:
        return chars[0].fullName
    else:
        return 'No characters found.'
    
@app.route('/seasons')
def seasons() -> str:
    seasons: list[Season] = db.session.query(Season).all()
    if seasons:
        return seasons[0].title
    else:
        return 'No seasons found.'
    

@app.route('/episodes')
def episodes() -> str:
    episodes: list[Episode] = db.session.query(Episode).all()
    if episodes:
        return episodes[0].title
    else:
        return 'No episodes found.'


@app.errorhandler(404)
def not_found(error) -> Response:
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
