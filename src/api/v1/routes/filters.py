from flask import Response

from api.v1.routes import app_routes
from api.v1.controllers.filters import filter_type_by_attributes


@app_routes.route('/filter', methods=['POST'])
def filter() -> Response:
    """
    Filters a type by attributes.

    Returns:
        A Flask Response object containing a JSON response
    """
    return filter_type_by_attributes()