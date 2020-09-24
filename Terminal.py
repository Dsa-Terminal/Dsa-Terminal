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
__version__ = '1.0.6'
# Importando modulos
import socket
from os import system, startfile, mkdir, listdir
from random import randint
from time import strftime, sleep
from rich.console import Console
from rich.markdown import Markdown
from tqdm import tqdm, trange
from rich.progress import track
# ==========================
system('title Dsa Terminal -i --login --bin\init.sh')
system('pause')
system(r'bin\bash.exe bin\init.sh')
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
def do_step(set, time):
    sleep(time)
def auto_get_ProgressBar(time):
    for step in track(range(100)):
        do_step(step, time)
class update:
    def __init__(self):
        system('title [Update] - Dsa Terminal')
        print('Lendo pacotes de https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(21)
        auto_get_ProgressBar(2)
        ProgressBar('Validando Serial')
        system('bin\git.exe pull')
        return True
class packge:
    def __init__(self):
        pass
    def pkg_install(command):
        cmd = command.replace('pkg install ', '')
        print(f'\033[32mLendo coleção https://github.com/Dsa-Terminal/{cmd}...'), sleep(8)
        print(f'Acessando archive do Dsa Terminal [{cmd}.git]'), sleep(4)
        auto_get_ProgressBar(1)
        ProgressBar('Baixando tools')
        system(fr'bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}.git')
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
        auto_get_ProgressBar(10)
        for d in range(0, 100):
            try:
                sleep(17.8)
            except KeyboardInterrupt:
                break
# Set up
ip = '0.0.0.0'
session = randint(0, 10364)
console = Console()
system('title Dsa Terminal')
print(strftime('Iniciando Dsa Terminal...'))
print(strftime(f'(C) %Y Dsa Terminal versão {__version__} Sessão: [{session}]'))
print(strftime('====================Dsa Terminal===================')), sleep(2.9)
while True:
    try:
        cmd: str = input(f'\033[32mroot@mainFrame20:~$\033[m ').strip()
        if cmd == 'ping /?':
            print('Ping: Listagem de parametros\n')
            print('ping                Conectar com um servidor')
            print('ping -v             Verifica se servidor existe')
            print('ping -nc [porta]    Escuta porta serial')
        elif cmd == 'pkg /?':
            print('Pkg: Listagem de parametros')
            print('Local dos pacotes na rede: https://github.com/Dsa-Terminal\n')
            print('pkg install [pkgname]      Instala pacotes')
            print('pkg uninstall [pkgname]    Desinstala pacotes')
            print('pkg update                 Atualiza versão instalada do Dsa Terminal')
        elif 'pkg install ' in cmd:
            packge.pkg_install(cmd)
            continue
        elif 'pkg uninstall ' in cmd:
            packge.pkg_uninstall(cmd)
            continue
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
            cmd = cmd.replace('nano ', '')
            cmd = cmd.replace('nano', '')
            if cmd == '':
                system(rf'usr\bin\nano.exe')
                system(f'move {cmd} files')
            else:
                system(fr'usr\bin\nano.exe /files/{cmd}')
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
            system(fr'bin\bash.exe /files/{cmd}')
        elif cmd == 'help':
            print('Comando:              Função:\n')
            print('echo([mensagem]):     Escreve mensagens na tela')
            print('pkg [parametros]      Gerenciador de pacotes')
            print('nano [arquivo]        Dsa Terminal E-ditor')
            print('ping [parametros]     Opções de rede remota')
            print('help                  Exibe ajuda')
            print('version               Exibe versão instalada')
            print('./[shell script]      Executa shell script')
            print('block                 Protetor de tela')
            print('st [Tarefa]           Começa uma tarefa do Windows')
            print('mkdir [pasta]         Cria uma pasta')
            print('touch [arquivo]       Cria um arquivo')
            print('incluide [modulo]     Importa modulo e o executa')
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
        elif cmd == 'cls':
            system('cls')
            continue
        elif cmd == 'version':
            print(__version__)
            continue
        elif 'st' in cmd:
            system(f'start {cmd[cmd.find("t") + 1 : ]}')
            continue
        elif cmd == 'pkg update':
            update.__init__()
            break
        elif 'mkdir' in cmd:
            cmd = cmd.replace('mkdir ', '')
            cmd = cmd.replace('mkdir', '')
            if cmd == '':
                pass
            else:
                system(fr'mkdir files\{cmd}')
            continue
        elif 'touch' in cmd:
            cmd = cmd.replace('touch ', '')
            cmd = cmd.replace('touch', '')
            if cmd == '':
                open(r'files\Novo arquivo.txt', 'wt+')
            else:
                open(f'files\cmd', 'wt+')
                print(f"CRIANDO ARQUIVO {cmd}..."), sleep(1)
                auto_get_ProgressBar(0.03)
                continue
        elif 'rm' in cmd:
            cmd = cmd.replace('rm ', '')
            cmd = cmd.replace('rm', '')
            if cmd == '':
                print('Remove: Insira um nome-de-arquivo')
            else:
                system(fr'del \files\{cmd}')
        elif 'rmdir' in cmd:
            cmd = cmd.replace('rmdir ', '')
            cmd = cmd.replace('rmdir', '')
            system(fr'del \files\{cmd}')
        elif cmd == 'ls':
            system(r'bin\bash.exe bin\listdir.sh')
            continue
        elif cmd == 'ipconfig':
            system('ipconfig')
            continue
        elif 'incluide' in cmd:
            cmd = cmd.replace('incluide ', '')
            cmd = cmd.replace('incluide', '')
            if cmd == '':
                print('Incluide: Modulo sem nome')
            else:
                auto_get_ProgressBar(0.01)
                system(fr'Lib\{cmd}\Main.exe')
        else:
            print(f'{cmd}: comando invalido!')
            continue
    except:
        continue
