from time import sleep
from os import system
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

with open('Mydatabase.sql') as database:
    database = database.read()
    
class UserDataBase:
    def __init__(self):
        cmd = None
        keyboard = ['sudo', 'root', 'pkg-get', 'setup']
        for key in keyboard:
            if self.startswith(key):
                cmd = self.replace(key, '')
        return cmd
    def route(cmd):
        if cmd is not None:
            return ip
        else:
            return None
    def run(rota, ip):
        if rota == ip:
            system(f'start "" "https://{rota}"')
            return 'IP Serverdev Iniciado!'
        else:
            return 'Caminho invalido!'

if __name__ == "__main__":
    cmd = input('CMD: ').strip()
    cmder = UserDataBase.__init__(cmd)
    rota = UserDataBase.route(cmd=cmder)
    print(UserDataBase.run(rota, ip))