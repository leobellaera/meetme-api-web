import os
from sqlalchemy import Column, String, Integer
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

class Like(db.Model):
    __tablename__ = 'like'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_1 = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user_2 = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user_1_liked = db.Column(db.Boolean, nullable=False)
    user_2_liked = db.Column(db.Boolean, nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    gender_interests = db.Column(db.String, nullable=False)
    interests = db.Column(db.String, nullable=True)
    register_date = db.Column(db.String, nullable=True, default=func.now())
    user_1 = db.relationship('Like',backref='user_1', primaryjoin=id==Like.user_1)
    user_2 = db.relationship('Like',backref='user_2', primaryjoin=id==Like.user_2)