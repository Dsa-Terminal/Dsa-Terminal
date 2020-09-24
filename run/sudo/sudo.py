from os import system
from random import randint, choice
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print('Para executar o [sudo] informe o IP do computador')
ipa: str = input('IP: ').strip()
if ipa == ip:
    print('Acesso Permitido!')
else:
    print('Acesso negado.')