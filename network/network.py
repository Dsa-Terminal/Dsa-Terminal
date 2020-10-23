# Importando __modulos__
from requests import get
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.003)
porta = 82
route = 'net-1: 10.0.0.155/255.255.255.0 gw 10.0.0.1'
print('')
def __init__():
    with open('requests.query', 'rt') as json:
        json = json.read()
        url: str = input('Url:\> ')
        try:
            img = (get(url, json))
        except:
            return 'Servidor fechado', json, url
        return img, json, url
result, json, url = __init__()
print(f'================================================================')
print(f'|Resposta do Servidor: [{result}] Url: [{url}]')
print(f'|Requests item: [{json}] Driver de Rede do Dsa Terminal')
print(f'|Rota: [{route}] Porta: [{porta}]')
print(f'================================================================')