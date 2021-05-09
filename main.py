import logging
from telegram.ext import Updater
from telegram import Bot
from telegram_utils import command_generator
import config
import sys

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s - %(message)s',
                    level=logging.INFO, filename="logs")
logger = logging.getLogger('main')


def main():
    logger.info('Loading configuration')
    updater = Updater(config.telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    command_generator.set_commands(dispatcher)
    updater.start_polling()
    logger.info('Bot Started')


def send_message(chat_id, mensaje):
    bot = Bot(config.telegram_token)
    bot.send_message(chat_id, ' '.join(mensaje))


def send_file(chat_id, archivo):
    bot = Bot(config.telegram_token)
    bot.send_document(chat_id=chat_id, document=open(archivo[0], 'rb'))


if __name__ == '__main__':
    args = sys.argv[1:]
    option = ''
    if len(args) > 0:
        option = args[0]
    if option == 'commands':
        command_generator.print_commands()
    elif option == 'message':
        if config.chat_id is None:
            send_message(args[1], args[2:])
        else:
            send_message(config.chat_id, args[1:])
    elif option == 'file':
        if config.chat_id is None:
            send_file(args[1], args[2:])
        else:
            send_file(config.chat_id, args[1:])
    else:
        main()

