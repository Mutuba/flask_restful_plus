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


# created_at = fields.Function(lambda obj: obj.created_at.isoformat())
# modified_at = fields.Function(lambda obj: obj.modified_at.isoformat())
    
    
    

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
            
    # def test_inactive_registered_user_login(self):
    #     """ Test for login of registered user but inactive """
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
    #         # query for the user and set status to inactive state
    #         user = User.get_by_email('johndoe@gmail.com')
    #         user.active=False
    #         save_changes(user)
    #         response = self.login_user()
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 'fail')
    #         self.assertTrue(data['message'] == 'Your account is not active yet')
    #         self.assertTrue(response.content_type == 'application/json')
    #         self.assertEqual(response.status_code, 401)
           
        # def confirm_vendor_token(self, token):
    #     return self.client.get(
    #     'api/v1/vendors/confirm/' + token,
    #     content_type='application/json'
    # ) 
            
    # def test_registered_with_wrong_email_format_vendor_email(self):
    #     """ Test vendor registration with wrong email format """
    #     self.register_vendor()
    #     with self.client:
    #         response = self.register_vendor_with_wrong_email_format()
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 'fail')
    #         self.assertTrue(
    #             data['message'] == 'Missing or wrong email format or password is less than six characters')
    #         self.assertEqual(response.status_code, 409)
    
   # def register_vendor_with_wrong_email_format(self):
    #     return self.client.post(
    #         'api/v1/vendors/',
    #         data=json.dumps(dict( 
    #             owner=dict(
    #                 email="johndoe@com",
    #                 username= "JohnDoe2",
    #                 password= "ThePreciousPassword"
    #             ),
                
    #             industry= "BEAUTY",
    #             mode_of_payment="BANK_ACCOUNT",
    #             business_email_address="westernseedcompany@gmail.com",
    #             contact_person ="Saleem",
    #             contact_person_contact="0724834583",
    #             bank_acc_number="0001234567589",
    #             description="We sell maize seed at farmer friendly prices",
    #             business_name="Western Seed Company Limited"
        
    #         )),
    #         content_type='application/json'
    #     )
    
    # v=Vendor.query.paginate()
    
    
    # def test_registered_vendor_confirm_token_with_invalid_token(self):
    #     """ Test for registered vendor confirm token with invalid confirmation token """
        
    #     with self.client:
    #         token = str(uuid.uuid4())
    #         confirm_token_resp = self.confirm_vendor_token(token)
    #         data = json.loads(confirm_token_resp.data)
    #         self.assertTrue(data['message'] == 'The confirmation link is invalid or has expired.')
    
    
# @api.route('/api/rec/<string:uid>')
# @api.doc(params={'uid': {'description': 'user UID'},
#                  'param1': {'description': 'blabla', 'in': 'query', 'type': 'int'}})
# class MyResource(Resource):
#     @api.doc(params={'param2': {'description': 'another param just for that get route',
#                                 'type': 'int', 'default': 1}})
#     def get(self, uid):
#         param2 = int(request.args.get('param2'))
#         param1 = int(request.args.get('param1'))
#         return {'uid': uid, 'params': param1 + param2}

#     def post(self, uid):
#         param1 = request.args.get('param1')
#         return {'uid': uid, 'params': param1}

# It creates two endpoints: GET /api/rec/123321?param1=1&param2=3 and PUT /api/rec/123321?param1=100500

# What is here:

# You may add additional non-path arguments to api.doc. 
# Though you can explicitly define them as 'in: 'query', it is not necessary; all params not in path are used as query params by default.
# You may add additional doc & params to separate method (like param2 for GET). They are also considered as query params.
# By default, all non-path params have 'required': False


# def get_paginated_list(results, url, page, per_page):
#     page = int(page)
#     per_page = int(per_page)
#     count = len(results)
#     if count < page or per_page < 0:
#         abort(404)
#     # make response
#     obj = {}
#     obj['page'] = page
#     obj['per_page'] = per_page
#     obj['count'] = count
#     # make URLs
#     # make previous url
#     if page == 1:
#         obj['previous'] = ''
#     else:
#         page_copy = max(1, page - per_page)
#         per_page_copy = page - 1
#         obj['previous'] = url + '?page=%d&per_page=%d' % (page_copy, per_page_copy)
#     # make next url
#     if page + per_page > count:
#         obj['next'] = ''
#     else:
#         page_copy = page + per_page
#         obj['next'] = url + '?page=%d&per_page=%d' % (page_copy, per_page)
#     # finally extract result according to bounds
#     obj['results'] = results[(page - 1):(page - 1 + per_page)]
#     return obj

# def get_paginated_list(model, url, page, per_page):
#     pagination_object = db.session.query(model).paginate(page=page, per_page=per_page, error_out=False)
#     count = len(pagination_object.items)
#     if count < page or per_page < 0:
#         abort(404)
    
#     # make response
#     obj = {}
#     obj['page'] = page
#     obj['per_page'] = per_page
#     obj['count'] = count
    
#     previous = None
#     if pagination_object.has_prev:
#         # page = page-1
#         obj['previous'] = url + '?page=%d&per_page=%d' % (page - 1, per_page)
        
#     nex = None
#     if pagination_object.has_next:
#         # page = page + 1
#         obj['next'] = url + '?page=%d&per_page=%d' % (page + 1, per_page)
        
#     results = vendors_schema.dump(pagination_object.items)
    
#     obj['results'] = results
    
#     return obj


# class CreditCard(Base):
#     __tablename__ = 'card'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=True)


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String(50))
#     lastname = Column(String(50))
#     fullname = column_property(firstname + " " + lastname)
#     credit_card = relationship(CreditCard, backref='report')
#     has_credit_card = column_property(
#         exists().where(CreditCard.user_id == id)
#     )

# john = User(id=1, firstname='John', lastname='Doe')
# session.add(john)
# session.commit()
# print(john.has_credit_card)
# # False
# johns_card = CreditCard(user_id=1)
# session.add(johns_card)
# session.commit()
# print(john.has_credit_card)
# True


# from sqlalchemy import (
#     Column,
#     Integer,
#     String,
#     Boolean,
#     ForeignKey,
#     DateTime,
#     Sequence,
#     Float
# )
# import datetime

# DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
# Base = declarative_base()

# class Book(Base):  #<------------------------- 
#     __tablename__  = "books"    #matches the name of the actual database table
#     id             = Column(Integer,Sequence('book_seq'),primary_key=True) # plays nice with all major database engines
#     name           = Column(String(50))                                    # string column need lengths
#     author_id      = Column(Integer,ForeignKey('authors.id'))              # assumes there is a table in the database called 'authors' that has an 'id' column
#     price          = Column(Float)
#     date_added     = Column(DateTime, default=datetime.datetime.now)       # defaults can be specified as functions
#     promote        = Column(Boolean,default=False) 
    
    
# product model
# brand model that owns product

# variations = a product variation out of product

# class Interval(object):
#     # ...

#     @hybrid_property
#     def length(self):
#         return self.end - self.start

#     @length.setter
#     def length(self, value):
#         self.end = self.start + value

#     @length.update_expression
#     def length(cls, value):
#         return [
#             (cls.end, cls.start + value)
#         ]

# session.query(Interval).update(
#     {Interval.length: 25}, synchronize_session='fetch')


# from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy import select, func

# Base = declarative_base()



# class SavingsAccount(Base):
#     __tablename__ = 'account'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     balance = Column(Numeric(15, 5))



# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)

#     accounts = relationship("SavingsAccount", backref="owner")


#     @hybrid_property
#     def balance(self):
#         return sum(acc.balance for acc in self.accounts)

#     @balance.expression
#     def balance(cls):
#         return select(func.sum(SavingsAccount.balance)).\
#                 where(SavingsAccount.user_id==cls.id).\
#                 label('total_balance')


# from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.hybrid import hybrid_property

# Base = declarative_base()

# class SavingsAccount(Base):
#     __tablename__ = 'account'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     balance = Column(Numeric(15, 5))



# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)

#     accounts = relationship("SavingsAccount", backref="owner")

#     @hybrid_property
#     def balance(self):
#         if self.accounts:
#             return self.accounts[0].balance
#         else:
#             return None

#     @balance.setter
#     def balance(self, value):
#         if not self.accounts:
#             account = Account(owner=self)
#         else:
#             account = self.accounts[0]
#         account.balance = value

#     @balance.expression
#     def balance(cls):
#         return SavingsAccount.balance



# from slugify import slugify  # among other things

# class Song(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(255))
#     slug = db.Column(db.String(255))

#     def __init__(self, *args, **kwargs):
#         if not 'slug' in kwargs:
#             kwargs['slug'] = slugify(kwargs.get('title', ''))
#         super().__init__(*args, **kwargs)

    # pits = Column(ARRAY(Integer))
    # stores = Column(ARRAY(Integer))
    
    # payment_method = db.Column(
    #     db.Enum(PaymentMethod), default=PaymentMethod.PAYMENT_ON_DELIVERY, nullable=True
    # )
    

# db.session.query(func.avg(ProductRating.rating).label("average_rating")).filter(ProductRating.product_id == self.id)
    

# class PaymentMethod(enum.Enum):
#         MPESA = "Mpesa"
#     CARD = "Card"
#     WALLET = "Wallet"
#     PAYMENT_ON_DELIVERY = "Payment on Delivery"



# def upgrade():
#     op.drop_constraint('experiments_name_key', 'experiments')



# def downgrade():
#     op.create_unique_constraint('experiments_name_key', 'experiments', ['name'])

    
# class UserSchema(Schema):
#     name = fields.String()
#     email = fields.String()
#     created_at = fields.DateTime()
#     since_created = fields.Method("get_days_since_created")
#     def get_days_since_created(self, obj):
#     return dt.datetime.now().day - obj.created_at.day

    # def is_owner(self, owner_id):
    #     """Checks if user is the owner."""
    #     if self.owner.id == owner_id:
    #         return True
    #     else:
    #         return False
    



# @staticmethod
# def get_by_id(product_rating_id):
#     """
#     Filter a product_rating by Id.
#     :param product_rating:
#     :return: ProductRating object or None
#     """
#     return ProductRating.query.filter_by(id=product_rating_id).first()




# @classmethod
# def bulk_create_or_none(cls, iterable, *args, **kwargs):
#     try:
#         return cls.bulk_create(iterable, *args, **kwargs)
#     except exc.IntegrityError as e:
#         db.session.rollback()
#         return None

#q.filter(cls.id.in_([2, 3, 5, 7, 11]))


# path = os.getcwd()
# # file Upload
# UPLOAD_FOLDER = os.path.join(path, "uploads")

# # Make directory if "uploads" folder not exists
# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# from uuid import uuid4


# def uniquify(string):
#     ident = uuid4().__str__()[:8]
#     return f"{ident}-{string}"


# class UserSchema(Schema):
#     name = fields.Str()
#     # password is "write-only"
#     password = fields.Str(load_only=True)
#     # created_at is "read-only"
#     created_at = fields.DateTime(dump_only=True)

#  sa.Enum(name='variationvariable').drop(op.get_bind(), checkfirst=False)

# permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))

    # def get_by_variation_variable(self, variable):
    #     """
    #     Check a variation_variable by their variable
    #     :param variable:
    #     :return: ProductVariationVariable or None
    #     """
    #     return db.session.query(self.model).filter_by(variable=variable).first()
    
    
# from datetime import datetime
# from marshmallow import Schema, fields, validates, ValidationError

# class CreateNoteInputSchema(Schema):
#     time_created = fields.DateTime(required=True)

#     @validates('time_created')
#     def is_not_in_future(value):
#         """'value' is the datetime parsed from time_created by marshmallow"""
#         now = datetime.now()
#         if value > now:
#             raise ValidationError("Can't create notes in the future!")
        # if the function doesn't raise an error, the check is considered passed
        
        
# from flask import Flask
# from celery import Celery

# broker_url = 'amqp://guest@localhost'          # Broker URL for RabbitMQ task queue

# app = Flask(__name__)    
# celery = Celery(app.name, broker=broker_url)
# celery.config_from_object('celeryconfig')      # Your celery configurations in a celeryconfig.py

# @celery.task(bind=True)
# def some_long_task(self, x, y):
#     # Do some long task
#     ...

# @app.route('/render/<id>', methods=['POST'])
# def render_script(id=None):
#     ...
#     data = json.loads(request.data)
#     text_list = data.get('text_list')
#     final_file = audio_class.render_audio(data=text_list)
#     some_long_task.delay(x, y)                 # Call your async task and pass whatever necessary variables
#     return Response(
#         mimetype='application/json',
#         status=200
#     )


# class QueryWithSoftDelete(BaseQuery):
#     def __new__(cls, *args, **kwargs):
#         obj = super(QueryWithSoftDelete, cls).__new__(cls)
#         with_deleted = kwargs.pop('_with_deleted', False)
#         if len(args) > 0:
#             super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
#             return obj.filter_by(deleted=False) if not with_deleted else obj
#         return obj

#     def __init__(self, *args, **kwargs):
#         pass

#     def with_deleted(self):
#         return self.__class__(db.class_mapper(self._mapper_zero().class_),
#                               session=db.session(), _with_deleted=True)

# version: '3.7'

# services:
#   web:
#     build: .
#     command: python manage.py run
#     volumes:
#       - .:/usr/src/app/
#     ports:
#       - 5000:5000
#     env_file:
#       - ./docker.env

#     depends_on:
#       - db

#   db:
#     image: postgres:12-alpine
#     volumes:
#       - postgres_data:/var/lib/postgresql/data/
#     env_file:
#       - ./docker.env

# volumes:
#   postgres_data:

# POSTGRES_USER=mutuba
# POSTGRES_PASSWORD=baraka11
# POSTGRES_DB=bumi_docker

# SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
# APP_SETTINGS=development

# DATABASE_URL=postgresql+psycopg2://mutuba:baraka11@localhost:5432/bumi_docker


# APP_MAIL_USERNAME="a99fdd287b5ab4"

# APP_MAIL_PASSWORD="bb30d740b00338"

# def upgrade():
#      op.alter_column('vendor', 'active', nullable=False, server_default=sa.schema.DefaultClause("0"))


# def downgrade():
#     op.alter_column('vendor', 'active', nullable=False, server_default=sa.schema.DefaultClause("1"))

    # price = db.Column(db.Numeric(precision=9, scale=2), nullable=False, default=0.00)
    # discount = db.Column(db.Numeric(precision=5, scale=2)c, nullable=False, default=0.00)
    
                # "price": fields.Float(
            #     required=False,
            #     description="The selling price of the product",
            #     example=9200.00,
            # ),
            # "discount": fields.Float(
            #     required=False,
            #     description="The allowed discount for the customers",
            #     example=0.50,
            # ),
            
# discount = fields.Decimal(as_string=True)


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_column('product', 'discount')
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('product', sa.Column('discount', sa.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=False, 
#                                       server_default='0.00'))


    # @property
    # def price(self):

    #     product_variations = self.variations
    #     variation_with_values_and_active = [
    #         variation_variable
    #         for variation_variable in product_variations
    #         if variation_variable.variation_values and variation_variable.active
    #     ]

    #     variation_values_min_prices = [
    #         variation_value.min_price
    #         for variation_value in variation_with_values_and_active
    #     ]
    #     return sum(variation_values_min_prices)

    # @property
    # def sale_price(self):

    #     product_variations = self.variations
    #     variation_with_values_and_active = [
    #         variation_variable
    #         for variation_variable in product_variations
    #         if variation_variable.variation_values and variation_variable.active
    #     ]
    #     variation_values_min_sale_prices = [
    #         variation_value.min_sale_price
    #         for variation_value in variation_with_values_and_active
    #     ]
    #     return sum(variation_values_min_sale_prices)
    
    # @property
    # def min_price(self):
    #     variation_values = self.variation_values
    #     prices = [
    #         variation_value.variation_value_price
    #         for variation_value in variation_values
    #         if variation_value.active
    #     ]
    #     return min(prices)

    # @property
    # def min_sale_price(self):
    #     variation_values = self.variation_values
    #     sale_prices = [
    #         variation_value.variation_value_sale_price
    #         for variation_value in variation_values
    #         if variation_value.active
    #     ]
    #     return min(sale_prices)
    # @api.response(code=404, model=_error, description='Not Found')
    
    



# @app.errorhandler(404)
# def resource_not_found(e):
#     return jsonify(error=str(e)), 404


# from flask import jsonify
# from instance import app


# class ApiException(Exception):
#     status_code = 400

#     def __init__(self, message, status_code=None, payload=None):
#         super().__init__()
#         self.message = message
#         if status_code is not None:
#             self.status_code = status_code
#         self.payload = payload


#     def to_dict(self):
#         rv = dict(self.payload or ())
#         rv["message"] = self.message
#         return rv




# @app.errorhandler(ApiException)
# def resource_not_found(e):
#     return jsonify(e.to_dict())

# queryset = queryset.filter(or_(Product.price==price, Product.sale_price == price)



