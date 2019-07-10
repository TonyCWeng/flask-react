import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# app instance
app = Flask(__name__)
api = Api(app)

# set app settings
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# db instance
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)


# test to check if website is running
class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }


api.add_resource(UsersPing, '/users/ping')
