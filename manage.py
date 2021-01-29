import os
import unittest
import datetime
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.auth.model import user

from app.auth.model import blacklist
from instance import create_app, db


from app.auth.model.user import User
from app.auth.model.user import Address
from app.auth.model.user import UserAddress
from app.auth.model.phone import Phone


from app.auth.model.user import Role
from app.auth.model.user import  Permission

from app.auth.model.employee import Employee
from app.auth.model.boss import Boss
from app.auth.model.engineer import Engineer
from app.auth.model.tag import Tag
from app.auth.model.category import Category
from app.auth.model.product import Product

from app.auth.model.author import Author
from app.auth.model.book import Book
from app.auth.model.mutuba import Mutuba

from app.auth import blueprint

from app.me.route.home import home_api

from app.me_2.route.home import home_api2


app = create_app(os.getenv('APP_SETTINGS'))

app.register_blueprint(blueprint)


app.register_blueprint(home_api, url_prefix='/api1')

app.register_blueprint(home_api, url_prefix='/api2')


app.app_context().push()


manager = Manager(app)


migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def dummy():
    for i in range(100):
        # Create a user if they do not exist.
        user = User(
            email=f"example{i}@bucketmail.com",
            password="123456",
            public_id=f"public_{i}", 
            username=f"example{i}", 
            registered_on=datetime.datetime.utcnow()
            )
        db.session.add(user)
        db.session.commit()

@manager.command
def address():
    for i in range(20):
        # Create a user if they do not exist.
        address = Address(name=f"Roy{i}")
        db.session.add(address)
        db.session.commit()
        
    

if __name__ == '__main__':
    manager.run()