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
        logger.error(f'A problem has ocurred sending this message, {remain} attempts remain.')
        if retries == 0:
            logger.error('There are no more attempts to send this message')
        else:
            telegram_responser(update, context, command_response, retries=remain)


def set_commands(dispatcher):
    for command_dict in commands:
        description = CommandDescription(**command_dict)
        logger.info(description)
        command = CommandCallable(callback=telegram_responser,
                                  use_arg=True,
                                  description=description.command,
                                  command=description.shell_command,
                                  use_response=description.use_response,
                                  text=description.text,
                                  no_callback=description.no_callback,
                                  group=description.group,
                                  ignore_output=description.ignore_output)
        # noinspection PyTypeChecker
        command_handler = CommandHandler(description.command, command)
        dispatcher.add_handler(command_handler)


def print_commands():
    print('Please, copy-paste the next list on the command description on telegram\n')
    for command_dict in commands:
        print(CommandDescription(**command_dict))
