export DJANGO_DATABASE='local'
# export DJANGO_DATABASE='mysql'
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
