web: python HairPR/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
web: python HairPR/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT HairPR/settings.py