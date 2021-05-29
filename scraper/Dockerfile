FROM python:3.8

COPY . /app
WORKDIR /app
RUN pip install pipenv 
RUN pipenv install

CMD pipenv run python ./scrap.py