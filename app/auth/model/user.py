from instance import db, flask_bcrypt
from alcohol.rbac.sqlalchemy import SQLAlchemyRBAC
from alcohol.mixins.sqlalchemy import SQLAlchemyEmailMixin,SQLAlchemyPasswordMixin
import datetime
import jwt
from app.auth.model.blacklist import BlacklistToken
from instance.config import key
# from app.auth.model.address import Address
# from app.auth.model.user_address import UserAddress
from app.auth.model.phone import Phone



class UserAddress(db.Model):
    __tablename__ = 'user_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), primary_key = True)
    
    
    
class User(db.Model, SQLAlchemyEmailMixin, SQLAlchemyPasswordMixin):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    addresses= db.relationship('Address', secondary = 'user_address')
    phones = db.relationship(Phone, backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
    
    
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
        

    @staticmethod  
    def decode_auth_token(auth_token):
            """
            Decodes the auth token
            :param auth_token:
            :return: integer|string
            """
            try:
                payload = jwt.decode(auth_token, key)
                is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
                if is_blacklisted_token:
                    return 'Token blacklisted. Please log in again.'
                else:
                    return payload['sub']
            except jwt.ExpiredSignatureError:
                return 'Signature expired. Please log in again.'
            except jwt.InvalidTokenError:
                return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)    

class Address(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    users = db.relationship('User', secondary='user_address')
    


    
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    
    
    
class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    
    
acl = SQLAlchemyRBAC(User, Role, Permission)