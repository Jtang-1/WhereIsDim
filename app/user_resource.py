from . import db
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from .models import UserModel
from flask import jsonify

# used to retrive passed in arguments
_user_post_args = reqparse.RequestParser()
_user_post_args.add_argument('email', type=str, help='Add email', required = True)
_user_post_args.add_argument('city', type=str, help='Add city', required = True)
_user_post_args.add_argument('country', type=str, help='Add country', required = True)
_user_post_args.add_argument('lng', type=str, help='Add lng', required = True)
_user_post_args.add_argument('lat', type=str, help='Add lat', required = True)


# define how an object should be serialized. Return using these fields (paired with @marshal_with)
_user_resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'city': fields.String,
    'country': fields.String,
    'lng': fields.Integer,
    'lat': fields.Integer
}   

class UserListResource(Resource):
    def get(self):
        #https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
        users = UserModel.query.order_by(UserModel.date_created).all()
        json_list=[i.serialize for i in users]
        return jsonify(json_list)
    #should also handle adding (post) to list

class UserResource(Resource):
    #handles getting(get), updating(put), & deleting (del)  individual tasks
    @marshal_with(_user_resource_fields)
    def get(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            #returns <Response 404> and the .json will be message
            abort(404, message = "Could not find user with that ID")
        return user, 200

    @marshal_with(_user_resource_fields)
    def post(self, user_id = None):
        args = _user_post_args.parse_args()
        #if need to check unique abort(409, message = "__ taken")
        User = UserModel(email = args['email'], city = args['city'], country = args['country'], lng = args['lng'], lat = args['lat'])
        db.session.add(User)
        db.session.commit()
        return User, 201
    

