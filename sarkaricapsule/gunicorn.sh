#!/bin/bash

NAME="sarkaricapsule"                                  # Name of the application
DJANGODIR=/var/www/scap_rev2/sarkaricapsule             # Django project directory
SOCKFILE=/var/www/scap_rev2/run/gunicorn.sock                   # we will communicte using this unix socket
LOGFILE=/var/www/scap_rev2/log/gunicorn.log
USER=webmaster                                        # the user to run as
GROUP=webmaster                                            # the group to run as
NUM_WORKERS=5                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=sarkaricapsule.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=sarkaricapsule.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Create the log directory if it doesn't exist
LOGDIR=$(dirname $LOGFILE)
test -d $LOGDIR || mkdir -p $LOGDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ..//venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-

