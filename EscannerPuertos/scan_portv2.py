# Parte1
#Edgar 2030467
# Importamos librerias requeridas
import socket
# Parte2 
# se define la funcion scan con la cual
# se utiliza sockets para probar diferentes
# puertos
def scan(addr, port):
	#Creando un nuevo socket
	socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# Estableciendo el timeout para el nuevo objeto tipo socekt
	socket.setdeafulttimeout(1)

	# Conexion exitosa devuelve0. Devuelve error en caso coentrario
	result= socket_obj.connect_ex((addr, port)) # Dirección y puertos en tupla.

	# Se cierra el objeto
	socket_obj.close()

	return result
#Parte3
# Lista de puertos a escanear
port=[21,22,25,80]

#Parte4
# bucle por todas las ip del rango 129.168.0.*
for i in range(1,255):
	addr="192.168.0.{}".format (i)
	for port in ports:
		result= scan(addr, port)
		if result == 0:
			print(addr, port, "OK")
		else:
			print(addr, port, "Failed")
