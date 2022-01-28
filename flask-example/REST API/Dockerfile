FROM python:latest

# Any working directory can be chosen as per choice like '/' or '/home' etc
# I have chosen /usr/app/src
WORKDIR /usr/app/flask/src

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py ./

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]