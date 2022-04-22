poetry run black --check --config pyproject.toml src/
poetry run flake8 src/ --count --select=E9,F63,F7,F82,F401 --show-source --statistics
poetry run pytest
