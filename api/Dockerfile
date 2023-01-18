FROM python:3.9
RUN mkdir /src
WORKDIR /src
RUN pip install pipenv
CMD pipenv install --system --deploy --ignore-pipfile && flask run --reload --port 80 --host 0.0.0.0
