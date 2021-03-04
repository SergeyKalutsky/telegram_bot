import os
from pathlib import Path

class DefaultConfig():
    PROJECT = "telegram_bot"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    DEBUG = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

    DEBUG = True

    BASEDIR = '/app/app/'
    UPLOAD_FOLDER = 'static/data'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/project.db'

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True