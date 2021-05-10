# Telegram Shell Bot

A bot to execute shell commands on linux through a bot commands from a Telegram Bot.

# Requirements
You would need a token from a telegram bot, you can create one calling to [BotFather](https://telegram.me/BotFather) and paste it in `config.py`.
Then please rename `config.py.example` and `commands.py.example` removing `.example` from their file names.

# Configuration
The current config vars for `config.py` are:

| Variable      | type     | Description                                                                                                                                                                                                |
| ---           | ---      | ---                                                                                                                                                                                                        |
| telegra_token | required | Telegram token from BotFather                                                                                                                                                                              |
| chat_id       | optional | Your unique chat_id for your personal use, if not setted, everyone can call your bot commands, you could see logs to get it or coul use [this bot](https://github.com/elshaio/telegram_heroku) to know it  |
| logs_file     | optional | A file to save logs from the bot, default `None`.                                                                                                                                                          |

# Installation
You would want to have `python3.6` at least, and I recommend to use virtualenv for running this bot, you could install them using this command.
```shell
sudo apt install -y python3 python3-pip
sudo python3 -m pip install -U pip virtualenv
```
Then, create a virtualenv on your current folder installation, activate it and install dependencies:
```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
And run the script `install.sh`, I will put here a copy of the script and what it does.
```shell
# Get information from your user
username=$(whoami)
pwdpath=$(pwd)
pythonpath="$pwdpath/venv/bin/python"
mainpath="$pwdpath/main.py"
servicepath="$pwdpath/telegram_shell.service"
# Substitute the information on telegram_shell.service
sed -i -e "s|{{username}}|$username|" telegram_shell.service
sed -i -e "s|{{pythonpath}}|$pythonpath|" telegram_shell.service
sed -i -e "s|{{mainpath}}|$mainpath|" telegram_shell.service
sed -i -e "s|{{pwdpath}}|$pwdpath|" telegram_shell.service
# Install the service on your system
sudo ln -s $servicepath /etc/systemd/system/telegram_shell.service
```
After run `install.sh` you can use the following commands:
```shell
# You could use any of the next commands
# start - start the bot
# stop - stop the bot
# status - see the current status of the bot
# enable - enable autostart of the bot
# disable - disable the autostart of the bot
sudo systemctl [command] telegram_shell.service
```


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
    'no_callback': False,
    // Optional, default None, chat_id of a group if you want to execute the commands through a group or super group
    'group': None,
    // Optional, default False, says if the output of command need to be ignored, useful on commands like ssh -fNR that
    // keep stdout open and prevents the execution to finish
    'ignore_output': True
}
```

Commands on `commands.py` will be loaded by `telegram_utils/command_generator.py` as telegram handlers, and will be handled by the telegram bot.

# Arguments
## commands
```shell
python main.py commands
```
Will show in the terminal a list of the commands on `commands.py` to copy-paste to bot father as a description for bot's commands.

## message
```shell
python main.py message [if not config.chat_id] long message
```
Sends a message using the telegram client, if you don't have any chat_if on `config.py`, you need to specify the chat id.

## archivo
```shell
python main.py file [if not config.chat_id] /route/to/file
```
Will send the file, chat_id works same as message
