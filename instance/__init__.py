from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_bcrypt import Bcrypt
from .config import config_by_name
from celery import Celery


db = SQLAlchemy()
flask_bcrypt = Bcrypt()
celery = Celery(__name__)

def create_app(config_name):
    app = Flask(__name__)
    
    
    app.config.from_object(config_by_name[config_name])
    
    celery.config_from_object(config_by_name[config_name])
    
    # Arrange for tasks to have access to the Flask app
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs) 
    celery.Task = ContextTask
    
    
    app.config['SWAGGER'] = {
        'title': 'Flask API Starter Kit',
        "version":'1.0',
        "description": 'A level up on flask restplus web service'
    }
        
    swagger = Swagger(app)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    flask_bcrypt.init_app(app)

    

    return app