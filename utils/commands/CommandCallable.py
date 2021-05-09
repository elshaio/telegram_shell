import shell_pipes as shell
import logging

logger = logging.getLogger('CommandCallable')


def _voidcallback():
    return None


class CommandCallable:

    def __init__(self, **kwargs):
        """
        Constructor for CommandCallable, it would use __call__ to be execute by telegram bot
        NOTE: use_response is to take inner CommandCallable the command response and send it to the callback
        ignore_output is to ignore completely the command response and force to receive an empty response for command
        :param callback: Callback function to be executed as response for shell command execution
        :param use_arg: Adds shell command response as arg for callback
        :param use_kwarg: Adds shell command response as kwarg command_response for callback
        :param description: Desc for logs, usually is equals to comnmand of command_dict, the command for telegram
        :param command: Shell command to be executed
        :param use_response: Says if the command response will be used
        :param text: Default text used for responses
        :param no_callback: Says if the callback will be executed for this command
        :param group: Telegram group for specific group executions
        :param ignore_output: Says if shell response will be used or default text will be used
        """
        self._callback = kwargs.get('callback', _voidcallback)
        self._use_arg = kwargs.get('use_arg', False)
        self._use_kwarg = kwargs.get('use_kwarg', False)

        self._description = kwargs.get('description', '')
        self._command = kwargs.get('command')
        self._use_response = kwargs.get('use_response', False)
        self._text = kwargs.get('text', 'Command Executed')
        self._no_callback = kwargs.get('no_callback', False)
        self._group = kwargs.get('group')
        self._ignore_output = kwargs.get('ignore_output', False)

    def __call__(self, *args, **kwargs):
        logger.info('Executing {}'.format(self._description))
        execute = False
        shell_command_arguments = args[0]['message']['text'].split(' ', 1)
        if len(shell_command_arguments) == 1:
            shell_command_arguments = ''
        else:
            shell_command_arguments = shell_command_arguments[1]
        chat = args[0]['message']['chat']
        logger.info(chat['id'])
        if self._group is not None:
            chat = args[0]['message']['chat']
            if chat['type'] in ['group', 'supergroup'] and chat['id'] == self._group:
                execute = True
        else:
            execute = True
        if execute:
            response = shell.execute(self._command + ' ' + shell_command_arguments, ignore_output=self._ignore_output)
            execution_response = '\n'.join(response)
        else:
            execution_response = 'You do not have permission to execute this command'
        if self._use_response and execution_response != '':
            to_response = execution_response
        else:
            to_response = self._text
        if self._use_arg:
            args = args + (to_response,)
        if self._use_kwarg:
            kwargs = dict(command_response=to_response, **kwargs)
        if not self._no_callback:
            # noinspection PyArgumentList
            self._callback(*args, **kwargs)
        if self._use_response:
            return
        else:
            return to_response
