from telegram.ext import CommandHandler
from utils.commands import CommandDescription, CommandCallable
from commands import commands
import telegram.error
import logging

logger = logging.getLogger('command_generator')


def telegram_responser(update, context, command_response, retries=3):
    try:
        update.message.reply_text(command_response)
    except telegram.error.TimedOut:
        remain = retries - 1
        logger.error('Hubo un problema al enviar mensaje, quedan {} intentos restantes'.format(remain))
        if retries == 0:
            logger.error('No hay más intentos de envío de mensajes')
        else:
            telegram_responser(update, context, command_response, retries=remain)


def set_commands(dispatcher):
    for command_dict in commands:
        description = CommandDescription(**command_dict)
        logger.info(description)
        command = CommandCallable(command=description.shell_command,
                                  callback=telegram_responser,
                                  use_response=description.response,
                                  text=description.text,
                                  no_callback=description.no_callback,
                                  description=description.command,
                                  use_arg=True,
                                  group_id=description.group_id)

        command_handler = CommandHandler(description.command, command)
        dispatcher.add_handler(command_handler)


def print_commands():
    print('Please, copy-paste the next list on the command description on telegram\n')
    for command_dictionary in commands.commands:
        description = CommandDescription(**command_dictionary)
        print('{} - {}'.format(description.command, description.description))
    print('\n')

