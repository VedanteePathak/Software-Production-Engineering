FROM python:latest

WORKDIR /src

COPY calculator.py ./

#CMD [ "chmod +x pycalculator.py" ]

CMD [ "python", "./calculator.py" ]

CMD [ "python", "./calculator.py", "sqrt", "9"]

CMD [ "python", "./calculator.py", "log", "2"]

CMD [ "python", "./calculator.py", "pow", "9", "2"]
