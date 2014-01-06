#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os.path
import time
import datetime
import traceback
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.autoreload
import tornado.web
import ProjectConfig
from tornado.options import define, options


define("port", default=8888, help="run on the given port", type=int)
define("address", default='127.0.0.1', help="run on the given address")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/test", TestHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_patch=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):
    pass


class TestHandler(BaseHandler):
    def get(self):
        self.write("Test Anngge")


def main():
    tornado.options.parse_command_line()
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, address=options.address)
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(io_loop)
    io_loop.start()


if __name__ == "__main__":
    main()
