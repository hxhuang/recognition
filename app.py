#!/bin/python
#
#
#
#
#
#

import simplejson as json, time
from tornado.web import RequestHandler, Application
import tornado.ioloop
import tornado.web
from src.reader import Reader

class handler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello, world")

    def post(self, *args, **kwargs):
        _file = self.request.files.get('file')
        _money = "0.00"

        if _file:
            _money = Reader.getMoney(_file[0])

        self.write(json.dumps({"money": _money, "time": int(time.time())}))


def app():
    return Application([
        (r"/", handler),
    ])

if __name__ == "__main__":
    app = app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()