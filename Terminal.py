"""
MIT License

Copyright (c) 2020 Dsa-Terminal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# Dsa Terminal codigo-fonte
__version__ = '1.0.4'
# Importando modulos
import socket
from os import system, startfile, mkdir, listdir
from random import randint
from time import strftime, sleep
from rich.console import Console
from rich.markdown import Markdown
from tqdm import tqdm, trange
# ==========================
system('title Dsa Terminal')
system('pause')
system('cls')
# Funções
def ProgressBar(titulo):
    with tqdm(total=100) as progressbar:
        for i in range(10):
            sleep(0.1)
            progressbar.update(10)
    progressbar = tqdm([2, 4, 6, 8, 10, 12, 14, 16])
    for item in progressbar:
        sleep(0.1)
        progressbar.set_description('{}: {}'.format(titulo, item))
    for i in trange(20):
        sleep(0.1)
        pass
    for i in tqdm(range(20)):
        sleep(0.5)
        pass
def git_bash(cmd):
    system(f'bin\git.exe {cmd}')
    return True
class packge:
    def __init__(self):
        pass
    def pkg_install(command):
        cmd = command.replace('pkg install ', '')
        print(f'Coleção {cmd}...'), sleep(8)
        ProgressBar('Instalando')
        system(fr'Bin\bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}')
        system(fr'move {cmd} Lib')
        return True
    def pkg_uninstall(command):
        cmd = command.replace('pkg install ', '')
        print(f'Recolhendo informações do pacote {cmd}...'), sleep(5.25)
        ProgressBar('Desinstalando')
        system(fr'del Lib\{cmd}')
        return True
class files:
    def __init__(self):
        pass
    def Write(filename, texto):
        try:
            a = open(filename, 'wt')
        except FileNotFoundError:
            return False
        else:
            a.write(texto)
            a.close()
    def CriarArquivo(filename):
        try:
            a = open(filename, 'wt+')
            a.close()
        except Exception as e:
            return False
        else:
            return True
    def ArquivoExiste(filename):
        try:
            a = open(filename, 'rt')
        except FileNotFoundError:
            return False
        else:
            return True
class ping:
    def __init__(self):
        pass
    def ping_connect(ip, porta):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.03)
        try:
            s.connect_ex(ip, porta)
        except:
            print(f'Erro ao se conectar com {ip}')
        else:
            print(f'Ping: {porta} Conectado! Iniciando comunicação...'), sleep(5.9)
            while True:
                try:
                    print(f'Ping ===> root@mainFrame20 (localhost)')
                    print(f'|Executando!!!')
                    print(f'Recebendo respostas do Servidor {ip}')
                except KeyboardInterrupt:
                    break
    def ping_ip_serverstate(ip, porta):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.03)
        try:
            s.connect_ex(ip, porta)
            s.close()
        except:
            print('Servidor inexistente!')
        else:
            print('Servidor encontrado!')
    def nc(porta):
        print(f'Ping: Escutando Porta: [{int(porta)}] ')
        sleep('17.8')
# Primeiro Uso
try:
    with open('Terminal.dll') as username:
        username = username.read()
except FileNotFoundError:
    print(f'Bem-vindo ao Dsa Terminal versão {__version__}!')
    print(f'Estamos configurando tudo para você usar o Bash do Terminal...'), sleep(13.1)
    ProgressBar('Instalando tools')
    while True:
        username: str = input('Username: ').strip().lower()
        if username == "":
            continue
        else:
            break
    files.CriarArquivo('Terminal.dll')
    files.Write('Terminal.dll', username)
    system('cls')
    print('Olá vamos te dar um tutorial rapido de como usar o Dsa Terminal')
    print('1 - Para ver todos os comandos digite "help"')
    print('2 - Para ver os parametros digite [comando] /?')
    print('3 - Para sair digite "exit"')
    system('pause')
    print("""
MIT License

Copyright (c) 2020 Dsa-Terminal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
    system('pause')
    system('cls')
# Set up
ip = '0.0.0.0'
session = randint(0, 10364)
console = Console()
print(strftime('Iniciando Dsa Terminal...'))
print(strftime(f'(C) %Y Dsa Terminal versão {__version__} Sessão: [{session}]'))
print(strftime('====================Dsa Terminal===================')), sleep(2.9)
while True:
    try:
        cmd: str = input(f'\033[32m{username}@mainFrame20:~$\033[m ').strip()
        if cmd == 'ping /?':
            print('Ping: Listagem de parametros\n')
            print('ping                Conectar com um servidor')
            print('ping -v             Verifica se servidor existe')
            print('ping -nc [porta]    Escuta porta serial')
        elif cmd == 'ping':
            ipa: str = input('IP: ')
            while True:
                try:
                    portal = int(input('Porta: '))
                except:
                    continue
                else:
                    break
            ping.ping_connect(ipa, portal)
            del ipa, portal
        elif cmd == 'ping -v':
            ipa: str = input('IP: ')
            while True:
                try:
                    portal = int(input('Porta: '))
                except:
                    continue
                else:
                    break
            ping.ping_ip_serverstate(ipa, portal)
            del ipa, portal
        elif 'git' in cmd:
            git_bash(cmd=cmd)
            continue
        elif 'ping -nc' in cmd:
            cmd = cmd.replace('ping -nc ', '')
            cmd = cmd.replace('ping -nc', '')
            if cmd == '':
                print('Ping: É necessario fornecer uma porta!')
            else:
                ping.nc(int(cmd))
        elif 'nano' in cmd:
            print('Dsa Terminal editor foi iniciado')
            system('title [Nano] - Dsa terminal')
            client = cmd.replace('nano ', '')
            cmd = cmd.replace('nano', '')
            system(rf'usr\bin\nano.exe {cmd}')
            system('title Dsa Terminal')
        elif 'echo(' in cmd:
            cmd = cmd.replace('echo(', '')
            cmd = cmd.replace('):', '')
            cmd = cmd.replace(r'\n', '\n')
            cmd = cmd.replace(r'\t', '\t')
            print(cmd)
            continue
        elif cmd == 'echo /?':
            print('Echo: Listagem de parametros\n')
            print(r'    echo([mensagem[parametros de formatação]]):')
            print(r'\t                Tab')
            print(r'\n                Quebra de linha')
        elif './' in cmd:
            cmd = cmd.replace('./', '')
            system(fr'bin\bash.exe {cmd}')
        elif cmd == 'help':
            print('Comando:              Função:\n')
            print('echo([mensagem]):     Escreve mensagens na tela')
            print('pkg [parametros]      Gerenciador de pacotes')
            print('nano [arquivo]        Dsa Terminal E-ditor')
            print('ping [parametros]     Opções de rede remota')
            print('help                  Exibe ajuda')
            print('./[shell script]      Executa shell script')
            print('block                 Protetor de tela')
            print('git [parametros]      Versionando com Git')
            print('exit                  Sai do Dsa Terminal')
        elif cmd == 'block':
            startfile('Bubbles.scr')
            continue
        elif cmd == '':
            for d in range(0, 1):
                continue
            del d
        elif cmd == 'exit':
            del cmd, username, session, ip, console
            break
        elif cmd == 'clear':
            system('cls')
            continue
        else:
            print(f'{cmd}: comando invalido!')
            continue
    except:
        continue
