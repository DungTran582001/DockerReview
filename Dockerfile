FROM python:3.9-buster
WORKDIR /core
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /core/app
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]