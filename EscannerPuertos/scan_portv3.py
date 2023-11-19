#Parte1
#Edgar 2030467
# Importamos librerias necesarias 
import sys
import threading
from socket import *

#Parte2
# Creamos una función tcp_test la cual
# permite probar mediante socket los peurtos
$ abiertos, se le agrega lock.release()
def tcp_test(port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result = 0:
		print "Opened port:" port

#PARTE3
#Establecemos el main del script
#Guardamos en la vairable host  y portstrs
if __name__='__main__':
	#portscan.py <host> <start_port>-<end_port>
	host = sys.argv[1]
	portstrs = sys.argv[2].split('-')
	
	# Parte4 
	#portstr se convierte en lista al momento
	# de hacer split y de ahi obtener los valores
	start_port = int(portstrs[0])
	end_port = int(portstrs[1])
	
	#Parte5
	# Usando la función gethostbyname se obtiene
	# la direccion ip
	target_ip= gethostbyname(host)
	
	#Parte6
	# Se inicia bucle para probar puertos
	#usando la funcion tcp_test y generando
	#un hilo por cada peurto a probar
	hilos=[]
	for port in rang(start_port, end_port):
		hilo = threanding.Thread(target=tcp_test, args=(port,))
		hilos.append(hilo)
		hilo.start()
