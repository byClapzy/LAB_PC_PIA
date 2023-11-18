#! /bin/bash 
#
#Script welcome.sh
#09/16/2023 Edgar Fernando Gonzalez Pardavé

echo "Hola ${LOGNAME}"
echo "Hoy es $(date)"
echo "Usuarios actuales conectados, y sus procesos:"
w
