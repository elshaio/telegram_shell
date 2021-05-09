# Telegram Shell Bot

Éste es un bot para la ejecución de comandos de shell en línux a travez de un comando de bot, éstos por elmmomento son fijos.

# Agregar comandos
Para agregar un nuevo comando al bot, es necesario editar el archivo `comandos.py` y agregar más elementos al array de diccionarios de la siguiente manera:
```javascript
{
    // Opcional, default Comando, Solo es utilizado para la descripción del comando commands
    'description': 'Soy una descripción',
    // Comando a ejecutar en telegram, en el bot se llama /comando
    'command': 'comando',
    // Comando de shell a ejecutar, éste puede ser a su vez un bash
    'shell_command': 'echo hola',
    // Opcional, default False, Indica si la respuesta del comando shell será enviada como respuesta del comando de telegram
    'use_response': True,
    // Opcional, default "Comando ejecutado", Es utilidado ya sea cuando el comando shell falla o cuando use_response es false y es necesario establecer una respuesta extra.
    'text': 'Soy un mensaje de respuesta',
    // Opcional, default False, Es utilizado para establecer si el callback que lanza la respuesta de telegram será ejecutado o no, si es True, no será enviada ninguna respuesta al cliente de telegram.
    'no_callback': False
    // Opcional, default None, chat_id de un group que sólo podrá ejecutar los comandos en un grupo
    'group': None
}
```

Los comandos establecidos en `comandos.py` serán cargados por el archivo `telegram_utils/command_generator.py` como handlers para los comandos de telegram, y serán puestos en escucha por el bot de telegram.

# Argumentos
## commands
Al ejecutar el comando:
```sh
python main.py commands
```

Éste imprimirá en terminal los comandos listados en `comandos.py` de manera conveniente para pegar en la descripción de comandos de telegram, éstos se toman de la manera `{comando} - {descripcion}`.

## mensaje
```sh
python main.py mensaje chat_id mensaje largo
```

Enviará un mensaje usando el cliente de telegram, util para bash.

## archivo
```sh
python main.py archivo chat_id /file
```
Enviará el archivo que se haya especificado.
