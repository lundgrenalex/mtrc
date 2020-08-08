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

update: git pull
build: update; docker-compose build
start: docker-compose up -d
stop: docker-compose down
restart: stop start
