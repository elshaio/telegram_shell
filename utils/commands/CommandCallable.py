from utils import shell


def _voidcallback():
    return


class CommandCallable:

    def __init__(self, **kwargs):
        self._command = kwargs.get('command')
        self._callback = kwargs.get('callback', _voidcallback)
        self._use_arg = kwargs.get('use_arg', False)
        self._use_kwarg = kwargs.get('use_kwarg', False)
        self._use_response = kwargs.get('use_response', False)
        self._text = kwargs.get('text', '')

    def __call__(self, *args, **kwargs):
        response = shell.execute(self._command)
        text = '\n'.join(response)

        if self._use_response:
            to_response = text
        else:
            to_response = self._text

        self._response = to_response

        if self._use_arg:
            args = args + (to_response,)

        if self._use_kwarg:
            kwargs = dict(command_response=to_response, **kwargs)

        self._callback(*args, **kwargs)
        return to_response

    def get_response(self):
        return self._response
