# Fastapi Clean Architecture
Fastapi Clean Architecture boilerplate.

## Requirements

- [Python 3.11](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/) for managing package / requirements

## Docs
`Docs url will be put in here in advance`

# Development

Copy `.env.example` to `.env` then install requirements:

```bash
pipenv install
# or
pip install -r requirements.txt
```
Start development server
```bash
pipenv run uvicorn app.main:app --reload
# or
uvicorn app.main:app --reload
```

## Migrations

We use [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) to manage database migrations.

### Generating migrations
```bash
pipenv run alembic revision -m "{your migration message}"
# or
alembic revision -m "{your migration message}"
```
Then the migration file will be generated at `./migrations/versions/{timestamp}_create_todos_table.py` directory

### Migrate

```bash
pipenv run alembic upgrade head
# or
alembic upgrade head
```

### Rollback
```bash
pipenv run alembic downgrade -1
# or
alembic downgrade -1
```

## Testing
Test files will be placed on `./tests` directory. All controllers test should be placed on `./tests/api` directory.

### Prepare database

Create database called `my_test_db` on your local machine.


### Running test
To run test you can use `pytest` command to do the job
```bash
# run all tests
pipenv run pytest
# or
pytest

# run specific test file
pipenv run pytest ./tests/path_to_your_test_file.py
# or
pytest ./tests/path_to_your_test_file.py

# run with verbose
pipenv run pytest -v
# or
pytest -v

# run with complete log
pipenv run pytest --capture=no
# or
pytest --capture=no
```

# Production

## Build docker image
```bash
docker build -t fastapi-clean-architecture .
```

## Run docker container
```bash
docker run -d -p 8000:8000 fastapi-clean-architecture --env-file .env
```
