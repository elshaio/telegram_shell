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
    logger.info('Iniciando configuración')

    updater = Updater(config.telegram_token, use_context=True)

    dispatcher = updater.dispatcher

    command_generator.set_commands(dispatcher)

    updater.start_polling()

    logger.info('Bot iniciado')


def enviar_mensaje(id, mensaje):
    bot = Bot(config.telegram_token)
    bot.send_message(id, ' '.join(mensaje))


def enviar_archivo(id, archivo):
    bot = Bot(config.telegram_token)
    bot.send_document(chat_id=id, document=open(archivo[0], 'rb'))


if __name__ == '__main__':
    args = sys.argv[1:]

    option = ''
    if len(args) > 0:
        option = args[0]

    if option == 'commands':
        command_generator.print_commands()
    elif option == 'mensaje':
        enviar_mensaje(args[1], args[2:])
    elif option == 'archivo':
        enviar_archivo(args[1], args[2:])
    else:
        main()

