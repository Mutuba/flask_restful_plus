from flask import request, jsonify
from flask_restplus import Resource
from ..util.user_dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, get_paginated_list
from ..service.schema import users_schema
from flask_restplus import fields, marshal, reqparse


# user_fields = {
#     'id': fields.Integer,
#     'username': fields.String,
#     'email': fields.String,
# }
# resource_fields = {
#     # 'count': fields.Integer,
#     # 'limit': fields.Integer,
#     # 'next': fields.String,
#     # 'previous': fields.String,
#     'results': fields.List(fields.Nested(user_fields)),
#     # 'start': fields.Integer choices=[10, 20, 30, 40, 50]
#     }



# @app.expect(model)        
# def post(self, id):
#   try:
#     list_of_names[id] = request.json['name']
#     return {
#       "status": "New person added",
#       "name": list_of_names[id]
#     }
#   except KeyError as e:
#     name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
#   except Exception as e:
# name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")


pagination = reqparse.RequestParser()

pagination.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination.add_argument('per_page', type=int, required=False, default=10)
 
 
api = UserDto.api
# _user for internal usage in the file only
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.expect(pagination)
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        args = pagination.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        users = get_all_users()
        data = users_schema.dump(users)
        return get_paginated_list(
            data, 
            '/user', 
            page=page, 
            per_page=per_page
            )

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user