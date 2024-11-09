.PYONY: clean

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	
lint: clean
	ruff format .
	ruff check --fix .

doctest:
	python -m doctest -v *.py

test:
	pytest -vvv .
