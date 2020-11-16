import socket

class Start_Terminal:
    run_cmd = 'Terminal --login -i'
    protocols = ['MINGW64', 'MSYS']
    protocol = protocols[1]
    dependences = ['flask', 'pygame', 'asyncio', 'sqlite3', 'sys', 'plataform', 'socket',
                   'os', 'random', 'time', 'getpass', 'tqdm', 'requests', 'rich.progress']
    module = '__main__'
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    start_pwd = '\home'
