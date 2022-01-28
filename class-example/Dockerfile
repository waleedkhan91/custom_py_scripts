FROM python:latest

LABEL Maintainer="Waleed Khan"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# I have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY myscript.py ./
# Now the structure looks like this '/usr/app/src/myscript.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./myscript.py"]
