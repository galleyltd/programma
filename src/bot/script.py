from confluent_kafka import Producer
from telegram.ext import Updater, CommandHandler, Job

print("hello galley")

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('YOUR TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
