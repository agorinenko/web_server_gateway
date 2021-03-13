from wsgi.wsgi_app import WSGIHandler
from wsgi.wsgi_server import run_with_cgi

if __name__ == '__main__':
    run_with_cgi(WSGIHandler)
