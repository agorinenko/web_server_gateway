import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ASGIHandler:
    def __init__(self, scope):
        assert scope["type"] == "http"
        self.scope = scope

    async def __call__(self, receive, send):
        logger.debug('Start request')
        logger.debug(self.scope)

        response_body = '{"text": "Hello world!"}'.encode('utf-8')
        headers = [
            (b'Content-type', b'application/json'),
            (b'Content-Length', str(len(response_body)).encode('utf-8')),
        ]

        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": headers,
        })

        await send({
            "type": "http.response.body",
            "body": response_body
        })
