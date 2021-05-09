# Telegram Shell Bot

A bot to execute shell commands on linux through a bot commands from a Telegram Bot.

# Add Commands
To add a new command to the bot, you need to add them to the file `commands.py` as a dict on the array on the following way.
```javascript
{
    // Optional, default Command, Just for description and maybe to generate description for telegram
    'description': 'I am a description',
    // Command to execute on telegram, in the bot is called as /command
    'command': 'command',
    // Shell command to execute, it could be a bash file
    'shell_command': 'echo Hello World',
    // Optional, default False, Sets if the response from the shell command will be used as response
    // to the telegram command, otherwise, text will be used.
    'use_response': True,
    // Optional, default "Command Executed", it is used when the shell command has an exit status different from 0 or
    // when use_response is setted to False and is necessary to set an extra response.
    'text': 'I am a message',
    // Optional, default False, Used to say if any response will be redirected to telegram, 
    // if True, nothing will happend on telegram side.
    'no_callback': False
    // Optional, default None, chat_id of a group if you want to execute the commands through a group or super group
    'group': None
}
```

Commands on `commands.py` will be loaded by `telegram_utils/command_generator.py` as telegram handlers, and will be handled by the telegram bot.

# Arguments
## commands
```sh
python main.py commands
```
Will show in the terminal a list of the commands on `commands.py` to to copy-paste to bot father as a description for bot's commands.

## message
```sh
python main.py message [if not config.chat_id] long message
```
Sends a message using the telegram client, if you don't have any chat_if on `config.py`, you need to specify the chat id.

## archivo
```sh
python main.py file [if not config.chat_id] /route/to/file
```
Will send the file, chat_id works same as message
