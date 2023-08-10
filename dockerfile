FROM python:3.11.2-slim-buster
WORKDIR /src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install pipenv
RUN apt update
COPY Pipfile Pipfile.lock /src/
RUN pipenv install --system --deploy
RUN pipenv --clear
COPY app /src/app

# this will serve on port 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
