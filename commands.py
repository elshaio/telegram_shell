commands = [
    {
        'description': 'Run a bash and responds Server Updated, this bash inside send messages and files',
        'command': 'updateserver',
        'shell_command': './assets/todos.sh',
        'use_response': False,
        'text': 'Server Updated',
    },
    {
        'description': 'Directly runs a command and return the response',
        'command': 'directcommand',
        'shell_command': 'docker ps -a --filter name=todos --format "table {{.Names}}\t{{.Status}}\t{{.CreatedAt}}"',
        'use_response': True,
    },
    {
        'description': 'Run a bash with the params of the command and return the response of bash',
        'command': 'bash_response',
        'shell_command': './assets/cambiar_rama.sh',
        'use_response': True,
        'group': 1234
    },
    {
        'description': 'Send the content of a file, put use_response to true',
        'command': 'catfile',
        'shell_command': 'cat ~/modulos.json',
        'use_response': True,
        'group': -1234
    }
]
