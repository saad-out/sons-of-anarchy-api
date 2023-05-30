from flask import (
    Flask,
    jsonify,
    make_response,
    Response,
)
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from os import getenv

from api.v1.models import *
from api.v1.routes import app_routes
from api.v1.utils.database import db
from api.v1.utils.config import Config

load_dotenv()

app: Flask = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
db.init_app(app)
migrate: Migrate = Migrate(app, db)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app.register_blueprint(app_routes)


@app.errorhandler(404)
def not_found(error) -> Response:
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host=getenv('APP_HOST', 'localhost'),
            port=int(getenv('APP_PORT', 5000)),
            debug=bool(getenv('DEBUG', False)))
