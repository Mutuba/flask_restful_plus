
# # from manage import app
# from main import celery

# # from flask import Flask

# # flask_app = Flask(__name__)

# # celery = make_celery(flask_app)

# @celery.task()
# def print_hello():
#     logger = print_hello.get_logger()
#     logger.info("Hello")
#     return "I am mutuba"


# @celery.task()
# def add_together(a, b):
#     return a + b

import click

from instance import (
    create_app,
    celery,
)
from instance import tasks


app = create_app()

@app.shell_context_processor
def make_shell_context():
    # Exports for `flask shell`
    return {
        # 'app' is exported automagically
        'celery': celery,
    }

@app.cli.command()
@click.argument('a')
@click.argument('b')
def add(a, b):
    task = tasks.add.delay(int(a), int(b))
    result = task.get()
    print("task {} said {}".format(task.id, result))