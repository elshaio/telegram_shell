class CommandDescription:
    def __init__(self, **kwargs):
        self.command = kwargs.get('command')
        self.shell_command = kwargs.get('shell_command')
        self.response = kwargs.get('use_response', False)
        self.text = kwargs.get('text', 'Comando ejecutado')
        self.no_callback = kwargs.get('no_callback', False)
