.PHONY: check lint format

check:
	pytest tests/ --cov=app --cov-report=term-missing

lint:
	flake8 app/ tests/

format:
	black app/ tests/

lint-fix:
	autopep8 --in-place --recursive app/ tests/