#!/bin/bash
set -e

exec gunicorn wsgi_app:WSGIHandler -b 0.0.0.0:8000 --log-level debug --timeout 5
