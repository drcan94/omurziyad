web: gunicorn backend.wsgi:application --log-file - --log-level
python manage.py collectstatic --noinput
manage.py migrate