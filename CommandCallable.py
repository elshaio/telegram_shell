import shell


def _voidcallback():
    return


class CommandCallable:

    def __init__(self, **kwargs):
        self._command = kwargs.get('command')
        self._callback = kwargs.get('callback', _voidcallback)
        self._response_arg = kwargs.get('response_arg', False)
        self._response_kwarg = kwargs.get('response_kwarg', False)

    def __call__(self, *args, **kwargs):
        response = shell.execute(self._command)
        text = '\n'.join(response)

        self.response = text

        if self._response_arg:
            args = args + (text,)

        if self._response_kwarg:
            kwargs = dict(command_response=text, **kwargs)

        self._callback(*args, **kwargs)
        return text

