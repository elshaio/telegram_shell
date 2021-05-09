#!/bin/bash
# Uses the params of the command
if [ -z "$1" ]
then
  exit 1
fi

if [ -z "$2" ]
then
  exit 1
fi

cd somefile/simco-front
linea=$(grep -n -A 2 "\"nombre\": \"$1\"" modulos.json  | tail -n1 | awk '{print $1}' | sed -e "s/-//g")
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo :V
else
  echo nel
  exit 1
fi
sed -i "${linea}s/.*/        \"version\": \"$2\"/" modulos.json
cat modulos.json

