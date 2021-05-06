import shell_pipes as shell
import logging

logger = logging.getLogger('CommandCallable')


def _voidcallback():
    return None


class CommandCallable:

    def __init__(self, **kwargs):
        self._command = kwargs.get('command')
        self._callback = kwargs.get('callback', _voidcallback)
        self._use_arg = kwargs.get('use_arg', False)
        self._use_kwarg = kwargs.get('use_kwarg', False)
        self._use_response = kwargs.get('use_response', False)
        self._text = kwargs.get('text', 'done')
        self._no_callback = kwargs.get('no_callback', False)
        self._description = kwargs.get('description', '')
        self._group_id = kwargs.get('group_id')

    def __call__(self, *args, **kwargs):
        logger.info('Ejecutando {}'.format(self._description))

        ejecutar = False

        text = args[0]['message']['text'].split(' ', 1)
        if len(text) == 1:
            text = ''
        else:
            text = text[1]

        chat = args[0]['message']['chat']
        logger.info(chat['id'])

        if self._group_id is not None:
            chat = args[0]['message']['chat']
            logger.info("chatmensaje = {}".format(chat))
            logger.info(self._group_id)

            if (chat['type'] == 'group' or chat['type'] == 'supergroup') and chat['id'] == self._group_id:
                ejecutar = True
        else:
            ejecutar = True

        if ejecutar:
            response = shell.execute(self._command + ' ' + text)
            text = '\n'.join(response)
        else:
            text = 'No se tienen permisos para ejecutar el comando'

        if self._use_response and text != '':
            to_response = text
        else:
            to_response = self._text

        self._response = to_response

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

    def get_response(self):
        return self._response
