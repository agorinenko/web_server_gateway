import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class WSGIHandler:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        logger.debug('Start request')
        logger.debug(self.environ)

        response_body = '{"text": "Hello world!"}'.encode('utf-8')
        status = '200 OK'
        headers = [
            ('Content-type', 'application/json'),
            ('Content-Length', str(len(response_body))),
        ]

        self.start_response(status, headers)

        yield response_body
