from flask import Blueprint

app_routes: Blueprint = Blueprint('app_routes', __name__, url_prefix='/api/v1')

from api.v1.routes.characters import *
from api.v1.routes.seasons import *
from api.v1.routes.episodes import *


@app_routes.route('/')
def index() -> str:
    return 'Routes for the Sons Of Anarchy API version 1 !'
