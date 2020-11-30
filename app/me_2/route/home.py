from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from app.me_2.model.welcome import WelcomeModel
from app.me_2.schema.welcome import WelcomeSchema

home_api2 = Blueprint('home2', __name__)



@home_api2.route('/me')
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