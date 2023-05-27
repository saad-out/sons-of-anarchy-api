from flask import (
    request,
    jsonify,
    Response,
    make_response
)
from datetime import (
    datetime,
    timedelta
)
from typing import Optional
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import jwt
import os

from api.v1.models.user import User

load_dotenv()


def login_user() -> Response:
    """
    """
    if not request.is_json:
        return make_response(jsonify({'message': 'Missing JSON in request'}), 400)

    credentials: dict = request.get_json()
    email: Optional[str] = credentials.get('email')
    if not email:
        return make_response(jsonify({'message': 'Missing email parameter'}), 400)
    password: Optional[str] = credentials.get('password')
    if not password:
        return make_response(jsonify({'message': 'Missing password parameter'}), 400)
    
    user: Optional[User] = User.query.filter_by(email=email).first()
    if not user:
        return make_response(jsonify({'message': 'User not found'}), 404)
    if not check_password_hash(user.password, password):
        return make_response(jsonify({'message': 'Invalid credentials.'}), 401)
    try:
        token: str = jwt.encode(
            {'firstName': user.firstName,
             'id': user.id,
             'exp': datetime.utcnow() + timedelta(hours=1)
            },
            os.environ.get('SECRET_KEY', ''),
            algorithm="HS256"
        )
        return make_response(jsonify({'token': token}), 201)
    except Exception:
        pass

    return make_response(jsonify({'message': 'Could not verify'}), 401)