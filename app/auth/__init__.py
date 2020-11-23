
from flask_restplus import Api
from flask import Blueprint

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API WITH JWT',
          version='1.0',
          description='A level up on flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)