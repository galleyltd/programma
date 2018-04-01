import logging
import sys

import tornado.ioloop
import tornado.web

from src.common.UserMessage import UserMessage
from src.common.WtfCommandMessage import WtfCommandMessage


class WtfHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        wtf_command = WtfCommandMessage(data["word"], data["username"])
        self.set_status(200)


class AllMessagesHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        message = UserMessage(data["text"], data["username"])
        self.set_status(200)


def get_logger():
    logger = logging.getLogger("programma")
    logger.setLevel(logging.DEBUG)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(
        logging.Formatter(
            fmt='%(asctime)s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    )
    logger.addHandler(screen_handler)
    return logger


def make_app():
    return tornado.web.Application([
        (r"/wtf", WtfHandler),
        (r"/messages", AllMessagesHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
