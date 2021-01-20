import os
from os import environ
# uncomment the line below for postgres database url from environment variable
postgres_database_url = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = 6379
    BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(
        host=REDIS_HOST, port=str(REDIS_PORT)))
    CELERY_RESULT_BACKEND = BROKER_URL
    
    # Celery Configuration
    broker_url = 'redis://localhost:6379'
    result_backend = 'redis://localhost:6379'
    # This keeps celery from screwing up logging on the Flask side
    celery_hijack_root_logger = False

class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = postgres_database_url
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_rest_plus_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = {  
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

key = Config.SECRET_KEY