web: python manage.py runserver
web: gunicorn MiningMachineryTracking.wsgi --log-file -
heroku config:set DISABLE_COLLECTSTATIC=1
heroku ps:scale web=1