export PYTHONPATH = "$PWD/lib"
export PIPENV_VENV_IN_PROJECT=1

install:
	@pipenv install -d

test:
	@pipenv run pytest

lint:
	@pipenv run pre-commit
