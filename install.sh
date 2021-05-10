#!/bin/bash
sudo echo Hi!
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
