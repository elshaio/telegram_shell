class CommandDescription:
    def __init__(self, **kwargs):
        self.description = kwargs.get('description', 'Command')
        self.command = kwargs.get('command')
        self.shell_command = kwargs.get('shell_command')
        self.use_response = kwargs.get('use_response', False)
        self.text = kwargs.get('text', 'Command Executed')
        self.no_callback = kwargs.get('no_callback', False)
        self.group = kwargs.get('group')
        self.ignore_output = kwargs.get('ignore_output', False)

    def __str__(self):
        return f"{self.command} - {self.description}"

