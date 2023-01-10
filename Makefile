export PYTHONPATH = "$PWD/lib"
export PIPENV_VENV_IN_PROJECT=1

install:
	@pipenv install

test:
	@pytest

lint:
	@pipenv run pre-commit
