# Parte 1
#Edgar 2030467
# Importamos librerias necesrias
import sys
import threading
import nmap
from socket import *

def escaneo_udp(host, start_port, end_port):
    target_ip = gethostbyname(host)
    opened_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            opened_ports.append(port)

    return opened_ports




'''---------------------------------------------------------------------------------------------------'''
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
'''----------------------------------------------------------------------------------------------'''

def tcp_test(port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result == 0:
		print ("Opened port:",port)

'''---------------------------------------------------------------------------------------------------'''

def escanear_red(ip_range):
    scanner = nmap.PortScanner()
    arguments = "-sn"  # Opción para realizar un escaneo de ping

    try:
        scanner.scan(hosts=ip_range, arguments=arguments)

        for host in scanner.all_hosts():
            if scanner[host]['status']['state'] == 'up':
                print(f"Host: {host} está activo")

    except Exception as e:
        print(f"Error al escanear la red: {e}")




while True:
    print("Menú:")
    print("OP1. Escaneo UDP:")
    print("OP2. Escaneo completo: ")
    print("OP3. Deteccion del sistema operativo:")
    print("OP4.Escaneo de red con ping   ")
    print("5. Salir")

    op = input("Selecciona una opción: ")

    #Parte3
    # Lista de puertos a escanear

    
    if op == 1:
        if len(sys.argv) != 4:
            print("Usage: python port_scan.py <host> <start_port> <end_port>")
        else:
            host = sys.argv[1]
            start_port = int(sys.argv[2])
            end_port = int(sys.argv[3])
            opened_ports = escaneo_udp(host, start_port, end_port)
            print("Puertos abiertos:")
            for port in opened_ports:
                print(port)
            
    if op == 2:

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

    if op == 3:
        
        host = sys.argv[1]
        portstrs = sys.argv[2].split('-')
        

        start_port = int(portstrs[0])
        end_port = int(portstrs[1])
        

        target_ip= gethostbyname(host)
        

        hilos=[]
        for port in range(start_port, end_port):
            hilo = threading.Thread(target=tcp_test, args=(port,))
            hilos.append(hilo)
            hilo.start()

    if op == 4:
        ip_range = "192.168.0.0/24"  # Rango de direcciones IP a escanear, ajusta según tus necesidades
        escanear_red(ip_range)

    if op == "5":
        print("Saliendo del programa.")
        break  # Sale del bucle while



