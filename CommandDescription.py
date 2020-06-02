class CommandDescription:
    def __init__(self, **kwargs):
        self.command = kwargs.get('command')
        self.shell_command = kwargs.get('shell_command')
        self.response = kwargs.get('response', False)
        self.text = kwargs.get('text', 'Comando terminado')
