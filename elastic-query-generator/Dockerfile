FROM python:latest

LABEL Maintainer="Waleed Khan"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# I have chosen /usr/app/src
WORKDIR /usr/app/elastic/src

#to COPY the remote file at working directory in container
COPY app.py ./
# Now the structure looks like this '/usr/app/src/myscript.py'

RUN pip3 install elasticsearchquerygenerator
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./app.py"]
