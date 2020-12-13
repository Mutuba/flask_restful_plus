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


# import flask_sqlalchemy

# db = flask_sqlalchemy

# class Pets(db.Model):
#     __abstract__ = True
#     name = db.Column(db.String(100))
#     price = db.Column(db.Integer)
#     breed = db.Column(db.String(100))

# class Cats(Pets):
#     __tablename__ = 'cats'
#     id = db.Column(db.Integer, primary_key=True)

# class Dogs(Pets):
#     __tablename__ = 'dogs'
#     id = db.Column(db.Integer, primary_key=True)

# My workaround solution that solves all my problems:

# I create a new List fields class (it is mainly copied from fields.List), 
# and then I just tune the output format and the schema in order to get the 'data' as key

# class ListData(fields.Raw):
#     '''
#     Field for marshalling lists of other fields.

#     See :ref:`list-field` for more information.

#     :param cls_or_instance: The field type the list will contain.

#     This is a modified version of fields.List Class in order to get 'data' as key envelope
#     '''
#     def __init__(self, cls_or_instance, **kwargs):
#         self.min_items = kwargs.pop('min_items', None)
#         self.max_items = kwargs.pop('max_items', None)
#         self.unique = kwargs.pop('unique', None)
#         super(ListData, self).__init__(**kwargs)
#         error_msg = 'The type of the list elements must be a subclass of fields.Raw'
#         if isinstance(cls_or_instance, type):
#             if not issubclass(cls_or_instance, fields.Raw):
#                 raise MarshallingError(error_msg)
#             self.container = cls_or_instance()
#         else:
#             if not isinstance(cls_or_instance, fields.Raw):
#                 raise MarshallingError(error_msg)
#             self.container = cls_or_instance
#     def format(self, value):

#         if isinstance(value, set):
#             value = list(value)

#         is_nested = isinstance(self.container, fields.Nested) or type(self.container) is fields.Raw

#         def is_attr(val):
#             return self.container.attribute and hasattr(val, self.container.attribute)

#         # Put 'data' as key before the list, and return the dict
#         return {'data': [
#             self.container.output(idx,
#                 val if (isinstance(val, dict) or is_attr(val)) and not is_nested else value)
#             for idx, val in enumerate(value)
#         ]}

#     def output(self, key, data, ordered=False, **kwargs):
#         value = fields.get_value(key if self.attribute is None else self.attribute, data)
#         if fields.is_indexable_but_not_string(value) and not isinstance(value, dict):
#             return self.format(value)

#         if value is None:
#             return self._v('default')
#         return [marshal(value, self.container.nested)]

#     def schema(self):
#         schema = super(ListData, self).schema()
#         schema.update(minItems=self._v('min_items'),
#                       maxItems=self._v('max_items'),
#                       uniqueItems=self._v('unique'))

#         # work around to get the documentation as I want
#         schema['type'] = 'object'
#         schema['properties'] = {}
#         schema['properties']['data'] = {}
#         schema['properties']['data']['type'] = 'array'
#         schema['properties']['data']['items'] = self.container.__schema__

#         return schema
       
    
# column_names = ['index', 'first_name', 'last_name', 'join_date']
# column_datatypes = ['integer', 'string', 'string', 'date']


# schema_dict = dict(zip(column_names, column_datatypes))
# print(schema_dict)
    # # mail settings
    
    
    # MAIL_SERVER='smtp.mailtrap.io',
    # MAIL_PORT=2525,
    # MAIL_USE_SSL=False,
    # EMAIL_USE_TLS = True,
    # # email authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

# user = User(email="tryme@gmail.com", password="123456", public_id="public_123123", username="Daniel243", registered_on=datetime.datetime.utcnow())

# def abort_vendor_doesnt_exist(vendor_id):
#     abort(404, message="Vendor {} doesn't exist".format(vendor_id))


        # token = generate_confirmation_token(new_vendor.owner.email)
        # confirm_url = f'http://localhost:5000/api/v1/vendor/confirm/{token}'
        
        # html = render_template('user/activate.html', confirm_url=confirm_url)
        
        
        # subject = "Please confirm your email"
        # # send_email(new_vendor.owner.email, subject, html)



# def generate_confirmation_token(email):
#     serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#     return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


# def confirm_token(token, expiration=86400):
#     serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#     try:
#         email = serializer.loads(
#             token,
#             salt=app.config['SECURITY_PASSWORD_SALT'],
#             max_age=expiration
#         )
#     except:
#         return False
#     return email

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
        
        
# @api.route('/confirm/<token>')
# @api.param('token', 'The token send to the user via email')
# @api.doc(responses={
#     200: 'Success',
#     400: 'The confirmation link is invalid or has expired.'
    
# })
# class ConfirmEmail(Resource):        
#     @api.doc('confirm vendor token send via email')
#     def get(self, token):
#         """
#         Confirm Vendor token send via email
#         :return: Http Json response
         
#         """
#         email = confirm_token(token)
#         if email:
#             user = User.get_by_email(email)
#             if user.confirmed:     
#                 response_object = {
#                     'status': 'success',
#                     'message': 'Account already confirmed. Cheers'
#                 }
#                 return response_object, 200     
#             else:
#                 user.active = True
#                 user.confirmed = True 
#                 user.confirmed_on = datetime.datetime.now()
#                 save_changes(user)
                
#                 response_object = {
#                     'status': 'success',
#                     'message': 'Account confirmed. Cheers!'
#                 }
#                 return response_object, 200 
                
#         else:
#             abort(400, 'The confirmation link is invalid or has expired.')
            
# from flask import render_template, Blueprint
# from itsdangerous import URLSafeTimedSerializer
# from flask_mail import Message
# from threading import Thread
# from instance import app, mail

# def send_email(to, subject, template):    
#     msg = Message(
#         subject,
#         recipients=[to],
#         html=template,
#         sender=app.config['MAIL_DEFAULT_SENDER']
#     )
#     mail.send(msg)
    
    # confirmed = db.Column(db.Boolean, nullable=False, default=False)
    # confirmed_on = db.Column(db.DateTime, nullable=True)
    

    # def test_registered_vendor_confirm_token(self):
    #     """ Test for registered vendor confirm token """
        
    #     with self.client:
    #         response = self.register_vendor()
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 'success')
    #         self.assertTrue(data['message'] == 'Vendor Successfully registered as vendor. Check your email for confirmation link')

    #         token = generate_confirmation_token('johndoe@gmail.com')
            
    #         confirm_token_resp = self.confirm_vendor_token(token)
    #         data = json.loads(confirm_token_resp.data)
    #         self.assertTrue(data['status'] == 'success')
    #         self.assertTrue(data['message'] == 'Account confirmed. Cheers!')
    
    
        # def test_registered_vendor_login(self):
    #     """ Test for login of registered vendor """
    #     with self.client:
    #         # vendor registration
    #         resp_register = self.register_vendor()
    #         data_register = json.loads(resp_register.data.decode())
    #         self.assertTrue(data_register['status'] == 'success')
    #         self.assertTrue(
    #             data_register['message'] == 'Vendor Successfully registered as vendor. Check your email for confirmation link'
    #         )
    #         token = generate_confirmation_token('johndoe@gmail.com')
    #         self.confirm_vendor_token(token)
 
    #         # registered vendor login
    #         response = self.login_vendor()
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 'success')
    #         self.assertTrue(data['message'] == 'Successfully logged in.')
    #         self.assertTrue(data['Authorization'])
    #         self.assertTrue(response.content_type == 'application/json')
    #         self.assertEqual(response.status_code, 200)
    
    
    
    # def test_registered_vendor_confirm_token_with_invalid_token(self):
    #     """ Test for registered vendor confirm token with invalid confirmation token """
        
    #     with self.client:
    #         token = str(uuid.uuid4())
    #         confirm_token_resp = self.confirm_vendor_token(token)
    #         data = json.loads(confirm_token_resp.data)
    #         self.assertTrue(data['message'] == 'The confirmation link is invalid or has expired.')


    # def test_unconfirmed_registered_user_login(self):
    #     """ Test for login of registered user but unconfirmed """
    #     with self.client:
    #         # user registration
    #         resp_register = self.register_user()
    #         data_register = json.loads(resp_register.data.decode())
    #         self.assertTrue(data_register['status'] == 'success')
    #         self.assertTrue(
    #             data_register['message'] == 'Successfully registered.'
    #         )
    #         self.assertTrue(data_register['Authorization'])
    #         self.assertTrue(resp_register.content_type == 'application/json')
    #         self.assertEqual(resp_register.status_code, 201)
    #         # registered user login
    #         # query for the user and set confirmed to false
    #         user = User.get_by_email('johndoe@gmail.com')
    #         user.confirmed=False
    #         save_changes(user)
    #         response = self.login_user()
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 'fail')
    #         self.assertTrue(data['message'] == 'Your account has not been confirmed yet')
    #         self.assertTrue(response.content_type == 'application/json')
    #         self.assertEqual(response.status_code, 401)
    
    
                # if not user.active:
                #     response_object = {
                #         'status': 'fail',
                #         'message': 'Your account is not active yet'
                #     }
                    
                #     return response_object, 401
                
                # if not user.confirmed:
                #     response_object = {
                #         'status': 'fail',
                #         'message': 'Your account has not been confirmed yet'
                #     }
                    
                #     return response_object, 401
                
                
            # token = generate_confirmation_token('johndoe@gmail.com')
            # self.confirm_vendor_token(token)
            