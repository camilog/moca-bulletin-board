#! /bin/bash

python manage.py drop
python manage.py db migrate
python manage.py db upgrade
