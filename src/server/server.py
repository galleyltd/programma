#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
import json

from tornado import gen, ioloop
import tornado.web
from motor.motor_tornado import MotorClient

from src.common.UserMessage import UserMessage
from src.common.WtfCommandMessage import WtfCommandMessage

from nltk.tokenize.stanford import CoreNLPTokenizer

sttok = CoreNLPTokenizer('http://corenlp:9000')

fake_stats = {}

client = MotorClient()


class WtfHandler(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        wtf_command = WtfCommandMessage(data["word"], data["username"])
        self.set_status(200)


class AllMessagesHandler(tornado.web.RequestHandler):
    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        message = UserMessage(data["text"], data["username"])
        await store_word_usage_stats(message.username, message.text)
        self.set_status(200)


class StatisticsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(
            json.dumps(sorted(fake_stats.items(), key=lambda x: x[1], reverse=True), ensure_ascii=False).encode('utf8'))
        self.set_status(200)


async def store_word_usage_stats(username, message):
    tokens = sttok.tokenize(message)
    for token in tokens:
        fake_stats[token.lower()] = fake_stats.get(token.lower(), 0) + 1
    await client.db.collection.update()


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
        (r"/messages", AllMessagesHandler),
        (r"/stats", StatisticsHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
