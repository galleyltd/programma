from telegram.ext import Updater, CommandHandler, MessageHandler, Job, Filters


def textMessageHandler(bot, update):
    print(update.message.from_user.first_name)
    #update.message.reply_text(
    #    'Your message: {}'.format(update.message.from_user.first_name))


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
