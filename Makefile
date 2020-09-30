DJTEST = python manage.py test shortner.tests -v 2
# These targets are not files

##################
# Install commands
##################
install: ## Create a poetry env and install dev and production requirements
	poetry shell
	poetry install


##################
# Tests and checks
##################
test:## Run tests
	@poetry run $(DJTEST)

##################
# Run flask dev server
##################
server:
	@poetry run python manage.py runserver
