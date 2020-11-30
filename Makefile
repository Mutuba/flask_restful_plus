.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv plus; \
	. plus/bin/activate; \
	pip install -r requirements.txt;

tests:
	. plus/bin/activate; \
	python manage.py test

run:
	. plus/bin/activate; \
	python manage.py run


dummy:
	. plus/bin/activate; \
	python manage.py dummy

all: clean install tests run