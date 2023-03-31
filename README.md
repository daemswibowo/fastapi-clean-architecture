# Fastapi Clean Architecture
Fastapi Clean Architecture boilerplate.

## Requirements

- [Python 3.11](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/) for managing package / requirements

## Docs
`Docs url will be put in here in advance`

# Development

Install requirements
```bash
pipenv install
# or
pip install -r requirements.txt
```
Start development server
```bash
uvicorn app.main:app --reload
```

## Migrations

We use [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) to manage database migrations.

### Generating migrations
```bash
alembic revision -m "create todos table"
```
Then the migrations file should be generated at `./migrations/versions/{timestamp}_create_todos_table.py` directory

### Migrate

```bash
alembic upgrade head
```

### Rollback
```bash
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
pytest

# run specific file test
pytest ./tests/path_to_your_test_file.py

# run with verbose
pytest -v

# run with complete log
pytest --capture=no
```

# Production
`Production docs will be put in here in advance`
