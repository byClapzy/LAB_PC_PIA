#!/bin/bash
#Edgar 2030467
# Script para listar procesos ejecutándose
# en el servidor.
#
## Variables
#
TIME=$(date +%d-%m-%Y_%H:%M:%S)
FECHA=$(date +%d-%m-%Y)
#
## Creando directorio de log
#
if [ ! -d "$HOME/log" ]; then
    mkdir "$HOME/log"
fi
#
## Listando procesos
#
LOG_FILE="$HOME/log/procesos_${FECHA}.log"
echo "#" >> "$LOG_FILE"
echo "#################################" >> "$LOG_FILE"
echo "#" >> "$LOG_FILE"
echo "Hora: $TIME" >> "$LOG_FILE"
ps -ef >> "$LOG_FILE"
echo "TOTAL DE PROCESOS: $(ps -ef | wc -l)" >> "$LOG_FILE"
echo "Hora: $TIME" >> "$LOG_FILE"

