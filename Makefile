format:
	isort .
	black .

install:
	poetry install

lint: black flake typing

black:
	black .

flake:
	flake8 .

typing:
	mypy .
