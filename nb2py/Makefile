CONVERTED = converted
NOTEBOOKS = 01_01_greet.ipynb 01_02_greet_2.ipynb

convert-dir:
	-mkdir -p $(CONVERTED)

convert: convert-dir
	@for nb in $(NOTEBOOKS); do \
		pyscript=$$(echo $$nb | sed 's/^[0-9_]*//' | sed 's/.ipynb//'); \
		jupyter nbconvert --to script $$nb --output "${CONVERTED}/$${pyscript}"; \
	done

test: convert
	pytest -vvv .

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} + 
	find . -name ".pytest_cache" -type d -exec rm -rf {} +
	find . -name ".ipynb_checkpoints" -type d -exec rm -rf {} +
	find converted -name "*.py" -type f -exec rm -f {} +