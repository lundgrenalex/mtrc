VIRTUALENV_NAME=.env

install_requirements:
	@echo "Install requirements.txt:"
	$(VIRTUALENV_NAME)/bin/pip install -r requirements.txt

clean:
	@echo "Cleaning Python compiled files:"
	find . -name __pycache__ -exec rm -fr {} +
	find . -name '*.pyc' -delete

create_venv:
	@echo "Creating virtual env:"
	python3 -m venv --clear $(VIRTUALENV_NAME)
	$(VIRTUALENV_NAME)/bin/pip install --upgrade pip

start_without_docker:
	$(VIRTUALENV_NAME)/bin/gunicorn application:app \
	--bind 0.0.0.0:8087 \
	--workers 1 \
	--worker-class gevent \
	--worker-connections=3000 \
	--backlog=1000 \
	--timeout 60 \
	--log-level=info \
	--pid ./run/mtrc.pid;


update: git pull
build: update; docker-compose build
start: docker-compose up -d
stop: docker-compose down
restart: stop start
