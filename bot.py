import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
mytoken = ''

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Help!')

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    
def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', bot, update.error)
    
def main():
    updater = Updater(token=mytoken, workers=10)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(CommandHandler('help', help))
    # dispatcher.add_error_handler()
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
