#!/bin/bash

cd /home/sreasons/apps/servicios/$1
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
pip3 install gunicorn
deactivate
#python3 manage.py runserver 0.0.0.0:8000 < /dev/null 