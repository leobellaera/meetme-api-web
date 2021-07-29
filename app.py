from flask import Flask
from flask_cors import CORS
from models import setup_db, db_drop_and_create_all
from api import api


def create_app():
    flask_app = Flask(__name__)
    setup_db(flask_app)
    CORS(flask_app)
    api.init_app(flask_app)
    # db_drop_and_create_all() todo only local?
    return flask_app


app = create_app()
