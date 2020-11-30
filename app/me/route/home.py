from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from app.me.model.welcome import WelcomeModel
from app.me.schema.welcome import WelcomeSchema


home_api = Blueprint('home', __name__)


# api.add_namespace(auth_ns)


@home_api.route('/hello')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeSchema
        }
    }
})
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = WelcomeModel()
    return WelcomeSchema().dump(result), 200