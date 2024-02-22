FROM ubuntu:latest

WORKDIR /src

COPY calculator.py ./

#CMD [ "chmod +x pycalculator.py" ]

#CMD [ "python", "./calculator.py" ]
