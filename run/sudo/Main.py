import socket
from os import system

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

keywords = ['sudo', 'pkg-get', 'install']

class sudo:
    def __init__(self):
        cmd = None
        for key in keywords:
            if self.startswith(key):
                cmd = self.replace(key, '')
        if cmd is not None:
            return cmd
        elif cmd == None:
            return cmd
        return cmd
    def Sudo_PhoenixVoid(self):
        if self == None:
            return self
        else:
            return ip
    def run(self, machine_KEY_local):
        if self == machine_KEY_local:
            system(f'start "" "https://{ip}"')
            return True
        else:
            return False
if __name__ == "__main__":
    cdu = input(': ')
    cmd = sudo.__init__(cdu)
    cmd = sudo.Sudo_PhoenixVoid(cmd)
    sudo.run(cmd, ip)