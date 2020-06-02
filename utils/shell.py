import shlex
import subprocess


def execute(command=''):
    if command == '':
        return ''

    commands = command.split("|")
    stdout = _execute_command_on_pipe(commands)

    response = []

    for line in stdout:
        cleanline = str(line).replace("b'", "").replace("\\n'", "")
        response.append(cleanline)

    return response


def _execute_command_on_pipe(commands_to_execute, stdin=None):
    if len(commands_to_execute) == 0:
        return ''

    args = shlex.split(commands_to_execute[0])
    p = subprocess.Popen(args, stdin=stdin, stdout=subprocess.PIPE)

    if len(commands_to_execute) > 1:
        return _execute_command_on_pipe(commands_to_execute[1:], p.stdout)
    else:
        return p.stdout
