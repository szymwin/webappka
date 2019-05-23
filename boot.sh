#!/bin/sh
#flask run --host=0.0.0.0
python manage.py recreate_db
python manage.py add_fake_data -n 100
gunicorn --bind 0.0.0.0:$PORT  manage:app