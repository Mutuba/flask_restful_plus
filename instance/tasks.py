
import celery
import logging


logger = logging.getLogger(__name__)

@celery.task
def add(a, b):
    logger.info("adding {} and {}".format(a, b))
    return a + b

@celery.task()
def add_together(a, b):
    return a + b