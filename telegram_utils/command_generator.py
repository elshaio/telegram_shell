from telegram.ext import CommandHandler
from utils.commands import CommandDescription, CommandCallable
import commands


def telegram_responser(update, context, command_response):
    update.message.reply_text(command_response)


def set_commands(dispatcher):
    for command_ditciontary in commands.commands:
        description = CommandDescription(**command_ditciontary)
        command = CommandCallable(command=description.shell_command,
                                  callback=telegram_responser,
                                  use_response=description.response,
                                  text=description.text,
                                  no_callback=description.no_callback,
                                  use_arg=True)

        command_handler = CommandHandler(description.command, command)
        dispatcher.add_handler(command_handler)

