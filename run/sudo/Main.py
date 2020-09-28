from rich.console import Console
from os import system

keywords = ['sudo', 'pkg', 'install', 'uninstall', 'update', 'setver']

console = Console()
class main:
    def __init__(self):
        cmd = None
        for key in keywords:
            if self.startswith(key):
                cmd = self.replace(key, '')
        if cmd is not None:
            return True
        elif cmd == None:
            return False
    def run(self):
        exec(f'{self}')
        return True
cmd = main.__init__(keywords[2])
if cmd == True:
    main.run(cmd)
