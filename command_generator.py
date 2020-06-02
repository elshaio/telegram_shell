from telegram.ext import CommandHandler
import config
from CommandCallable import CommandCallable
from CommandDescription import CommandDescription


def telegram_responser(update, context, command_response):
    update.message.reply_text(command_response)


def set_commands(dispatcher):
    for command_ditciontary in config.comandos:
        description = CommandDescription(**command_ditciontary)
        command = CommandCallable(command=description.shell_command,
                                  callback=telegram_responser,
                                  response_arg=description.response)

        command_handler = CommandHandler(description.command, command)
        dispatcher.add_handler(command_handler)

