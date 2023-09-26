# This makefile was made for linux systems

VENV = .env
PY = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ACTIVATE = $(VENV)/bin/activate
MAIN = manage.py

# Virtual Enviroment
$(ACTIVATE): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

venv: $(ACTIVATE)
	echo "Virtual enviroment created"

activate: $(ACTIVATE)
	. $(ACTIVATE)
	echo "Virtual enviroment activated"

# Setup Server
db: $(ACTIVATE)
	$(PY) $(MAIN) makemigrations
	$(PY) $(MAIN) migrate

run: $(ACTIVATE) db
	$(PY) $(MAIN) runserver

# Cleaners
clean: 
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: run clean
