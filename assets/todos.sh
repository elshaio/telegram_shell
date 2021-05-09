#!/bin/bash
# Send message
./mensaje.sh actualizando simco-front
docker build -t something --rm --build-arg CACHEBUST=$(date +%s) --no-cache /some/folder > ~/dockerbuildtodos.log
# Send file
./archivo.sh ~/dockerbuildtodos.log

# At the end, sends the command message

