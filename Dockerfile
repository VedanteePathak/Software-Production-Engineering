FROM python:latest

WORKDIR /src

COPY calculator.py /src/

CMD [ "./calculator.py" ]