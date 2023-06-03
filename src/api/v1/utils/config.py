"""
This module contains the configuration for the API.
"""
import os
from dotenv import load_dotenv


load_dotenv()


POSTGRES_HOST = os.environ.get('POSTGRES_HOST', '')
POSTGRES_USER = os.environ.get('POSTGRES_USER', '')
POSTGRES_USER_PASSWORD = os.environ.get('POSTGRES_USER_PASSWORD', '')
POSTGRES_DB = os.environ.get('POSTGRES_DATABASE', '')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_USER_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False