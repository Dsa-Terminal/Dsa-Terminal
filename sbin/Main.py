#!/Python3/Scripts/python.exe
# Importando Módulos
from time import sleep
from random import randge, randint, random
import socketserver as sock_server
from rich.console import Console
from os import system
import socket
# Settings
console = Console()
# Function
def main(ip, conn, route, port, host, server, app="__main__", path="/sbin/Main.py"):
	if conn is not bool:
		raise TypeError("Conexão Não foi estabelecida com o servidor só entende dados booleanos como verdadeiro e fo")
    	else:
		if route.startswith("net-1: "):
			if port < 1028:
				if host.upper() == "IPV4":
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				else:
			     		print("O Dsa Terminal só se conecta pelo provedorIPV4 do Sistema de criptografia UTF-16")
			else:
		     		print("O Dsa Terminal só pode se conectar com porta antes de 1028 pois são ligadas a serviços avançados")
		     		return False
		else:
	     		print("As rotas são definidas como net- e o host do provedor de rede")
	     		return False
main()
