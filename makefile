.PYONY: clean

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

doctest:
	python -m doctest -v *.py

test:
	pytest -vvv .