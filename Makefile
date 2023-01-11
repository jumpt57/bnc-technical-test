export PYTHONPATH = "$PWD/lib"
export PIPENV_VENV_IN_PROJECT=1

run:
	@pipenv run python lib/standardize.py

install:
	@pipenv install -d

test:
	@pipenv run pytest

test-cov:
	@pipenv run pytest --cov

lint:
	@pipenv run pre-commit

export-requirements:
	@pipenv run pip freeze > requirements.txt
