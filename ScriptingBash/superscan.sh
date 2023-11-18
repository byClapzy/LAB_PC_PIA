#!/bin/bash
#
##Script superscan.sh
#09/16/2023 Edgar Fernando Gonzalez Pardavé

# Ejemplo de Menu en BASH
#
date
    echo "||"
    echo "||===========================||"
    echo "||   Menu Principal          ||"
    echo "||===========================||"
    echo "||I. Net Discover"
    echo "||II. Port scan v1"
    echo "||III. welcome"
    echo "||IV. Exit"
    echo "||"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $ubi./Netdiscover.sh;;
        2) $ubi./portscanv1.sh;;
        3) $ubi./welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac

