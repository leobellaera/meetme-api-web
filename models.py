import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


def setup_db(app):
    database_path = os.getenv('DATABASE_URL', 'sqlite:///meet_me.db')
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    gender_interests = db.Column(db.String, nullable=False)
    interests = db.Column(db.String, nullable=True)
    register_date = db.Column(db.String, nullable=True, default=func.now())
