import os
from flask_marshmallow import Schema
from marshmallow.fields import Str, Integer,Nested
from flask_marshmallow import Marshmallow



class AddressSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["id", "name"]

    id = Integer()
    name = Str()


class UserSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["id", "email", "username", 'address_id', 'public_id']

    id = Integer()
    email = Str()
    username = Str()
    public_id = Str()
    address_id = Integer()

user_schema = UserSchema()
users_schema = UserSchema(many=True)