import logging
from telegram.ext import Updater
from command_generator import set_commands
import config

logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s',
                    level=logging.INFO)


def main():
    logging.info('Iniciando configuración')

    updater = Updater(config.telegram_token, use_context=True)

    dispatcher = updater.dispatcher

    set_commands(dispatcher)

    updater.start_polling()

    logging.info('Bot iniciado')


if __name__ == '__main__':
    main()

