FROM python:latest

WORKDIR /src

COPY calculator.py /src/pycalculator.py

#CMD [ "chmod +x pycalculator.py" ]

#CMD [ "./pycalculator.py" ]
