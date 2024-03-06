#!/bin/bash

set -e

gunicorn \
    --bind 0.0.0.0:8080 budgetplanner.project.wsgi:application \
    --timeout ${GUNICORN_TIMEOUT:-300} \
    --workers 3
;;
