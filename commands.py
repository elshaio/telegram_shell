commands = [
    {
        'command': 'ip',
        'shell_command': 'ifconfig eno1 | head -n2 | tail -n1 | awk \'{print $2}\'',
        'response': True
    }
]