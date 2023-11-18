n#!/bin/bash
#
# Ejemplo de Menu en BASH
#
date
    echo "||"
    echo "||===========================||"
    echo "||   Menu Principal          ||"
    echo "||===========================||"
    echo "||I. Net Discover"
    echo "||II. Actual User"
    echo "||III. Hostname"
    echo "||IV. Exit"
    echo "||"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $ubi./Netdiscover.sh;;
        2) whoami;;
        3) echo "Tu host es:"
                hostname
                echo "saludos";;
        4) echo "Bye!"; exit 0;;
esac
