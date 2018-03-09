export DJANGO_DATABASE='local'
# export DJANGO_DATABASE='mysql'
python manage.py makemigrations
python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application --reload
# gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application --daemon --reload
