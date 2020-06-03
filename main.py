import logging
from telegram.ext import Updater
from telegram_utils import command_generator
import config
import sys

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger('main')


def main():
    logger.info('Iniciando configuración')

    updater = Updater(config.telegram_token, use_context=True)

    dispatcher = updater.dispatcher

    command_generator.set_commands(dispatcher)

    updater.start_polling()

    logger.info('Bot iniciado')


if __name__ == '__main__':
    args = sys.argv[1:]

    option = ''
    if len(args) > 0:
        option = args[0]

    if option == 'commands':
        command_generator.print_commands()
    else:
        main()

