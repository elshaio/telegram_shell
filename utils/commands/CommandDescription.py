class CommandDescription:
    def __init__(self, **kwargs):
        self.command = kwargs.get('command')
        self.shell_command = kwargs.get('shell_command')
        self.response = kwargs.get('use_response', False)
        self.text = kwargs.get('text', 'Command Executed')
        self.no_callback = kwargs.get('no_callback', False)
        self.description = kwargs.get('description', 'Command')
        self.group_id = kwargs.get('group')
        self.ignore_output = kwargs.get('ignore_output', False)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}".format(self.command, self.shell_command, self.response, self.text, self.no_callback, self.description, self.group_id)

