#!/bin/bash

if [ -z "$PORT" ]
  then export PORT=8000
fi
if [ -z "$DATABASE_URL" ]
  then export DATABASE_URL="sqlite:///""$DBPATH""/db.sqlite"
fi
if [ -z "$FSN" ]
  then export FSN=""
fi
if [ ! -z "$MIGRATE" ]
  then "$MAINDIRECTORY"/manage.py migrate && "$MAINDIRECTORY"/manage.py migrate base
fi
if [ ! -z "$COLLECTSTATIC" ]
  then "$MAINDIRECTORY"/manage.py collectstatic --noinput --clear
fi
if [ ! -z "$CREATE_SUPERUSER" ]
  then if [ -z "$DJANGO_SUPERUSER_PASSWORD" ]
    then export DJANGO_SUPERUSER_PASSWORD="admin"
  fi
  if [ -z "$DJANGO_SUPERUSER_EMAIL" ]
    then export DJANGO_SUPERUSER_EMAIL="test@example.com"
  fi
  if [ -z "$DJANGO_SUPERUSER_USERNAME" ]
    then export DJANGO_SUPERUSER_USERNAME="admin"
  fi
  "$MAINDIRECTORY"/manage.py createsuperuser --noinput
fi

uwsgi --plugins=python --http-socket=0.0.0.0:"$PORT" --pidfile=/tmp/infodb.pid --home="$VENVPATH" --module=infodb.wsgi:application --chdir="$MAINDIRECTORY" --static-map /static="$SROOT"
