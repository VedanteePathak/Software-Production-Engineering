FROM python:latest

WORKDIR /src

COPY calculator.py /src/pycalculator.py

CMD [ "./pycalculator.py" ]
