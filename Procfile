web: guncorn app:app
web: python manage.py runserver 0.0.0.0:$PORT --noreload
release: pyton manage.py makemigrations --no-input
web: gunicorn capstone_pro.wsgi
manage.py migrate
web: gunicorn capstone_pro.wsgi:application --log-file - --log-level debug
