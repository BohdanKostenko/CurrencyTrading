FROM python:3.10-slim

WORKDIR /usr/src/CurrencyTrading

RUN pip3 install pipenv

COPY trading.py ./trading.py

COPY Pipfile ./Pipfile

COPY Pipfile.lock ./Pipfile.lock

RUN pipenv install --deploy --ignore-pipfile

ADD test_csv /usr/src/CurrencyTrading/test_csv

ENTRYPOINT ["pipenv", "run", "python3", "./trading.py"]

CMD [""]