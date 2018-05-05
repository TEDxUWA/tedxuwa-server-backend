#!/bin/sh
# This is a manual deployment script for ease of life. Would be much
# better if we have an auto deployment system like git hooks
# but I haven't been able to set it up yet

# THIS ASSUME YOU'RE IN THE /

# clear all screens
pkill screen
# front end deployment
cd ../front-end/
git checkout origin/master
npm build
# back end deployment
cd ../back-end/
git checkout origin/master
source env/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput  # collect front end
python manage.py migrate  # migrate the database
python manage.py runserver 0.0.0.0:8000  # start the server on port 8000