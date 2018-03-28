import tornado.ioloop
import tornado.web

from src.common.TelegramMessage import TelegramMessage


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.set_status(500)
        self.write({"key": "value"})


def make_app():
    tgMsg = TelegramMessage("fdsfds")
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/error", ErrorHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
