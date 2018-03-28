import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.set_status(500)
        self.write({"key": "value"})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/error", ErrorHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
