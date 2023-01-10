export PYTHONPATH = "$PWD/lib"
export PIPENV_VENV_IN_PROJECT=1

install:
	@pipenv install
	@pre-commit install

test:
	@pytest
