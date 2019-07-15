from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import User
from sqlalchemy import exc

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

# Controllers 
class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid params'
        }
        if not post_data:
            return response_object, 400
        username = post_data.get('username')
        email = post_data.get('email')
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                db.session.add(User(username=username, email=email))
                db.session.commit()
                response_object['status'] = 'success'
                response_object['message'] = f'{email} was added'
                return response_object, 201
            else:
                response_object['message'] = 'That Email is already in use.'
                return response_object, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400


api.add_resource(UsersList, '/users')


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'ping!'
        }

api.add_resource(UsersPing, '/users/ping')