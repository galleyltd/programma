#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Job, Filters
from src.common.UserMessage import UserMessage

def textMessageHandler(bot, update):
    try:
        message = UserMessage(update.message.text, update.message.from_user.first_name)
        print(json.dumps(message.__dict__, ensure_ascii=False).encode('utf8'))
        requests.post('http://server:8888/messages',
                      data=json.dumps(message.__dict__, ensure_ascii=False).encode('utf8'))
    except Exception as inst:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args

def wtfCommandHandler(bot, update):
    update.message.reply_text(
        'WTF {}'.format(update.message.from_user.first_name))


if __name__ == "__main__":
    print("hello galley")
    updater = Updater('')

    updater.dispatcher.add_handler(MessageHandler(Filters.text, textMessageHandler))
    updater.dispatcher.add_handler(CommandHandler('wtf', wtfCommandHandler))

    updater.start_polling(clean=True)
    updater.idle()
