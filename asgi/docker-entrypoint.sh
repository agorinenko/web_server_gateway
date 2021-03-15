#!/bin/bash
set -e

# exec uvicorn asgi_app:ASGIHandler --host 0.0.0.0 --port 8000 --log-level debug --timeout-keep-alive 5
exec gunicorn asgi_app:ASGIHandler -b 0.0.0.0:8000 --log-level debug --timeout 5 -k uvicorn.workers.UvicornWorker
