web: python manage.py runserver
web: gunicorn MiningMachineryTracking.wsgi --log-file -
heroku ps:scale web=1