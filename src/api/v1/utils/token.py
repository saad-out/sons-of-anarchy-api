"""
This module contains the token_required decorator.
"""
from flask import request, jsonify, Response
from functools import wraps
from typing import Union, Tuple, Optional, Mapping, Callable
from dotenv import load_dotenv
import jwt
import os

from api.v1.models.user import User

load_dotenv()


def token_required(view: Callable) -> Callable:
    """
    A decorator that checks for a valid JWT token in the request headers.
    
    Args:
        view (Callable): The view function to decorate.
        
    Returns:
        A wrapper function that either returns a response or calls the view function.
    """
    @wraps(view)
    def wrapper(*args, **kwargs) -> Union[Tuple[Response, int], Callable]:
        token: Optional[str] = request.headers.get('x-access-tokens')
        if not token:
            return jsonify({'message': 'a valid token is missing'}), 401
        try:
            data: Mapping = jwt.decode(token, os.environ.get('SECRET_KEY', ''), algorithms=["HS256"])
        except Exception:
            return jsonify({'message': 'token is invalid'}), 401
        return view(*args, **kwargs)
    return wrapper