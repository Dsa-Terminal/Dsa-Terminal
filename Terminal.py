__version__ = '3.8.5 > Plus'
from time import strftime, sleep
from tqdm import tqdm, trange
from random import random, randint, choice, choices
from rich.console import Console
from rich.table import Table
from os import system, startfile, mkdir, removedirs, remove, walk
import socket
system('title Dsa Terminal')
system('cls')
yeil = False
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
def matrixe(AF_INET):
    chars_to_print = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', ' ']
    hall = True
    for c in range(0, AF_INET):
        try:
            for i in range(100):
                print(choice(chars_to_print), end='', sep='')
            print(i)
        except KeyboardInterrupt:
            hall = None
            break
    if hall == True:
        print('Compilação completa')
    print('\n')
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
def pkg_install(command):
    cmd = command.replace('pkg install ', '')
    cmd = cmd.capitalize()
    print(f'Coleção {cmd}...'), sleep(8)
    print(f'   (87MB) Instalando dependencias.........'), sleep(5.967)
    print(f'      Criando cache...'), sleep(6.29)
    ProgressBar('Instalando')
    system(fr'Bin\bin\git.exe clone https://github.com/Felipe-Souza-Pereira-Lima/{cmd}')
    system(fr'move {cmd} Bin\Lib')
    print('Instalação completa.')
    Write(fr'Bin\Lib\Main.scl', fr'{cmd}\n')
    return True
class ping:
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
    def ping_set_connection(ip, porta):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.03)
        try:
            s.connect_ex(ip, porta)
        except:
            print(f'Conecção invalida com {ip} ===> Porta fechada!')
        else:
            matrixe(130)
class device:
    serverdev = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __localhost__ = f'Drivelocal: /dev/{serverdev}'
    def __init__():
        print('Procurando Hardwares em: /dev/...'), sleep(3.0)
        print(device.__localhost__)
'''pkg install DsaRepositories'''
session = randint(0, 99999999)
console = Console()
if __name__ == '__main__':
    system('title Dsa Terminal')
    system('PAUSE')
    system('cls')
    print(strftime(fr'Iniciando Dsa Terminal....'))
    print(strftime(fr'(C) %Y Dsa Terminal\IP: 23.354.816-54\Session: {session} '))
    print(strftime(fr'========================Dsa Terminal========================='))
    sleep(1.99)
    while True:
        try:
            client: str = input('\033[32mroot@mainFrame20:~$\033[m ').strip()
            if 'pkg install ' in client:
                pkg_install(client)
                continue
            elif 'ping ' in client:
                if client == 'ping --conn':
                    while True:
                        try:
                            ip = input('IP: ')
                            porta = int(input('Porta: '))
                        except:
                            continue
                        else:
                            break
                    ping.ping_connect(ip, int(porta))
            elif client == 'power':
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Ranger", style="dim", width=19)
                table.add_column("Power")
                table.add_column("Sexo", justify="right")
                table.add_row("Agente Red", "Magia da lua", "Masculino")
                table.add_row("Agente Yeloow", "Poder da fenix", "Feminino",)
                console.print(table)
            elif client == 'compile':
                ProgressBar('Compilando')
                system('cls')
                sleep(4.5)
                matrixe(AF_INET=randint(1000, 99999999999))
            elif client == 'device':
                device.__init__()
                continue
            elif client == 'python':
                try:
                    system('cls')
                    print('Python Console de Rede do Dsa Terminal')
                    ProgressBar()
                    startfile('Python')
                except:
                    print('Essa ação necessita Python 3 instalado')
                system('title Dsa Terminal')
            elif client == 'ipconfig':
                print('IP: [23.354.816-54] Porta: [8291]')
                print('DNS: [192.168.1.1] root@localhost')
            elif 'exec(python(' in client:
                client = client.replace('exec(python(', '')
                client = client.replace(')):', '')
                print('Carregando arquivo para o Dsa Terminal executor...')
                ProgressBar('Carregando')
                try:
                    system('cls')
                    startfile(client)
                except FileNotFoundError:
                    print('Arquivo não encontrado!')
                except:
                    print('Essa ação necessita Python 3 instalado')
            elif 'echo(' in client:
                client = client.replace('echo(', '')
                client = client.replace('):', '')
                client = client.replace(r'\n', '\n')
                client = client.replace(r'\t', '\t')
                print(client)
                continue
            elif client == 'dir':
                system(r'dir C:\Users\%username%')
                pass
            elif client == 'time':
                print(strftime('Hora: [%I:%M %p]Data: [%A\%e\%Y]'))
                continue
            elif client == 'ipset':
                system('ipconfig')
                pass
            elif client == 'nslookup':
                startfile('Bubbles.scr')
                print('Proteção de tela iniciada')
            elif client == 'cls':
                system('cls')
                continue
            elif client == 'version':
                print(__version__)
                continue
            elif client == 'session':
                print(session)
                pass
            elif client == 'reboot':
                print('Finalizando Dsa Terminal...'), sleep(5)
                startfile('Terminal.exe')
                break
            elif 'wait(' in client:
                client = client.replace('wait(', '')
                client = client.replace(')', '')
                time = float(client)
                sleep(time)
                continue
            elif 'exit' in client:
                system('pause')
                print('Encerrando o Dsa Terminal...')
                ProgressBar('Encerrando')
                break
            elif client == 'start':
                startfile('Terminal.exe')
                continue
            elif client == 'rootdir':
                system(r'echo Diretorio Raiz: %systemroot%')
                continue
            elif client == 'version(win32)':
                system('ver')
                pass
            elif client == 'exit(bios)':
                startfile('Bin\BIOS.html')
                break
            elif 'help' in client:
                print('|Comando:           |Função:                                |')
                print('|                   |                                       |')
                print('|dir                |Lista diretorios do usuario            |')
                print('|sc query           |Cataloga dados da BIOS                 |')
                print('|echo(text):        |escreve uma mensagen na tela           |')
                print('|help               |Exibe ajuda                            |')
                print('|start              |Inicia um novo Terminal                |')
                print('|version(win32)     |Exibe versão do windows                |')
                print('|ipset              |Configuração de Ip do windows          |')
                print('|wait(second)       |Espera segundos citados                |')
                print('|cls                |Limpa o console                        |')
                print('|time               |Exibe data e hora                      |')
                print('|nano               |Inicia o Dsa Terminal Editor           |')
                print('|reboot             |Reinicia o Dsa Terminal                |')
                print('|nslookup           |Inicia proteção de tela                |')
                print('|ipconfig           |Mostra o local de rede do Dsa Terminal |')   
                print('|rootdir            |Exibe Diretorio do sistema             |')
                print('|open(app local)    |Abre aplicativos e localhost           |')
                print('|python             |Inicia Python 3 console                |')
                print('|version            |Mostra a versão do Dsa Terminal        |')
                print('|load(value):       |Realiza upload de dados                |')
                print('|clear(load):       |Deleta os dados do upload              |')
                print('|prompt             |Suspende console                       |')
                print('|auto()             |Hacker signal Ethernet                 |')
                print('|session            |Exibe codígo da sessão                 |')
                print('|exit               |Finaliza o Dsa Terminal                |')
                continue
            elif 'nano' in client:
                print('Dsa Terminal editor foi iniciado')
                system('title [Nano] - Dsa terminal')
                client = client.replace('nano ', '')
                client = client.replace('nano', '')
                system(rf'D:\HIMEM\Bin\usr\bin\nano.exe {client}')
                system('title Dsa Terminal')
            elif client == 'sc query':
                system('sc query')
            elif 'open(' in client:
                client = client.replace('open(', '')
                if 'web(' in client:
                    client = client.replace('web(', '')
                    client = client.replace(')):', '')
                    print('Tentando resolver localhost para o navegador...')
                else:
                    client = client.replace('):', '.exe')
                    client = client.replace('.exe.exe', '.exe')
                    print('Procurando Aplicativo!')
                try:
                    ProgressBar()
                    startfile(client)
                except:
                    print('Esse programa não existe.')
                else:
                    print(f'{client} foi iniciado com sucesso')
                continue
            elif 'load(' in client:
                client = client.replace('load(', '')
                client = client.replace('):', '')
                __value_insc__ = client
                sleep(3.7)
                print('Upload completo!')
                continue
            elif client == 'setver':
                try:
                    print(__value_insc__)
                except:
                    print("Você precisa fazer upload de dados para velos")
                continue
            elif r'\n' in client:
                print('')
                continue
            elif client == 'clear(load):':
                del __value_insc__
                print('Deletado.')
                continue
            elif client == 'prompt':
                system('pause')
                print('')
                pass
            elif client == 'sys':
                system('systeminfo')
                system('pause')
            else:
                print('Comando invalido ou erro de sintax')
                continue
        except:
            print('\n')
            continue
