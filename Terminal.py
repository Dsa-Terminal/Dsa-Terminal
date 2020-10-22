# Licensa de uso do Dsa Terminal
"""
MIT License

Copyright (c) 2020 Dsa-Software

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
__version__ = '1.0.9'
# Importando modulos
import socket
from os import system, startfile, mkdir, listdir
from random import randint, choice
from time import strftime, sleep
from getpass import getpass
from rich.console import Console
from tqdm import tqdm, trange
from rich.progress import track
from requests import get
# ==========================
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
route = 'net-1: 10.0.0.155/255.255.255.0 gw 10.0.0.1'
porta = 82
# Barra de Progresso Tradicional
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
# Configurador de Barra
def do_step(set, time):
    sleep(time)
    pass
# Barra de Progresso Padrão
def auto_get_ProgressBar(time):
    for step in track(range(100)):
        do_step(step, time)
# Atualizador do Dsa Terminal
def update():
    system('title [Update] - Dsa Terminal')
    print('Lendo pacotes de https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(2.8)
    auto_get_ProgressBar(0.1)
    print('\033[mDecodificando Setups para o Compilador GitBoster (info).'), sleep(1.99)
    ProgressBar('Validando Serial')
    system('bin\git.exe pull')
    print(f'Setup de versão {__version__} Anterior <==== Update selected')
    return True
# Configuração do atualizador
class packge:
    def __init__(self):
        pass
    def pkg_install(command):
        cmd = command.replace('pkginstall ', '')
        cmd = command.replace('pkginstall', '')
        if cmd == '':
            print('Pkg: Insira-um-nome-de-pacote-valido')
        elif cmd == 'Dsa-Terminal':
            print('Pkg: Para atualizar o Dsa Terminal você deve usar o comando "pkg update"')
        else:
            print(f'Lendo coleção https://github.com/Dsa-Terminal/{cmd}...'), sleep(8)
            print(f'Acessando archive do Dsa Terminal [{cmd}.git]'), sleep(4)
            auto_get_ProgressBar(0.001)
            ProgressBar('Baixando tools')
            system(fr'bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}.git')
            system(fr'move {cmd} Lib')
            return True
    def pkg_uninstall(command):
        cmd = command.replace('pkg uninstall ', '')
        print(f'Recolhendo informações do pacote {cmd}...'), sleep(5.25)
        ProgressBar('Desinstalando')
        system(fr'del Lib\{cmd}')
        return True
    def pkg_update(command):
        cmd = command.replace('pkg update ', '')
        print(f'\033[32mLendo coleção https://github.com/Dsa-Terminal/{cmd}...'), sleep(8)
        print(f'Acessando archive do Dsa Terminal [{cmd}.git]'), sleep(4)
        auto_get_ProgressBar(1)
        ProgressBar('Baixando tools')
        system(rf'del Lib\{cmd}')
        system(fr'bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}.git')
        system(fr'move {cmd} Lib')
        return True
# Controlador de arquivos
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
# Ping network Servidor
class ping:
    def __init__(self):
        system('ping')
        return True
    def connect(self, ip):
        system(f'ping -t {ip}')
        return True
# iPXE
def iPXE():
    system('cls')
    print('iPXE -- Open Source Network Boot Firmware -- http://ipxe.org')
    print('Features: HTTP iSCSI DNS TFTP AoE FCoE TFTP COMBOOT ELF PXE PXEXT\n'), sleep(9.2)
    while True:
        cmd: str = input('iPXE> ')
        if cmd == 'route':
            print(route)
        elif cmd == 'sanboot':
            sleep(9.1)
            system('cls')
            print(strftime('Iniciando Dsa Terminal...'))
            print(strftime(f'(C) %Y Dsa Terminal v{__version__} Sessão: [{session}]'))
            print(strftime('====================Dsa Terminal=====================')), sleep(0.08)
            return True
            break
        elif cmd == 'boot':
            cmd = input('Boot Image in ServerLocal: ').strip().lower()
            try:
                img = get(cmd)
            except:
                print("iPXE: Server Webhost don't existent")
            else:
                print(img)
        elif cmd == '':
            continue
        elif cmd == 'exit':
            sleep(11.9)
            return False
            break
        elif cmd == 'ping':
            print('iPXE: Your network Firmware connection is variable!')
            print(f'iPXE: Network COMBOOT IP: {ip}\n')
        else:
            print(f'{cmd}: iPXE command not found!')
# Compile emulador
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
# Inicalizar
def __init__():
    system(r'cls')
    system(r'title Dsa Terminal -i --login --bin\init.sh')
    system(r'pause')
    if files.ArquivoExiste(fr'boot\boot.ini'):
        if files.ArquivoExiste(rf'boot\init.sh'):
            if files.ArquivoExiste(r'boot\drivers\pass.exc'):
                with open(r'boot\drivers\pass.exc', 'rt') as key:
                    key = key.read()
                    password = getpass('Password: ').strip()
                    if password == key:
                        system('cls')
                        return True 
            else:
                print('Registre uma palavra-passe para o Dsa Terminal!\n')
                while True:
                    password = getpass('Password: ').strip()
                    if password == '':
                        print('Insira uma palavra-passe!')
                    else:
                        with open(r'boot\drivers\pass.exc', 'wt+') as key:
                            files.Write(r'boot\drivers\pass.exc', password)
                            system('cls')
                            break
                return True
        else:
            return False
    else:
        return False
# Set up
console = Console()
session = randint(0, 291462)
# Configurações do iPXE Boot 
start = __init__()
# Inicialização normal
if start == True:
    # Leitura de Senha
    with open(r'boot\drivers\pass.exc', 'rt') as key:
        key = key.read()
    # Variaveis globais
    root = "/"
    pwd = "/files"
    # Sistema
    system('cls')
    system('title Dsa Terminal')
    print(strftime('Iniciando Dsa Terminal...'))
    print(strftime(f'(C) %Y Dsa Terminal v{__version__} Sessão: [{session}]'))
    print(strftime('===================Dsa Terminal==============')), sleep(0.08)
    while True:
        try:
            system(f'echo ┌─────────[\033[32m%username%@%computername%\033[m] \033[34m~\033[m')
            cmd: str = input(f'└─$ ').strip()
            # Listagem de parametros do Pkg
            if cmd == 'pkg /?':
                print('Pkg: Listagem de parametros')
                print('Local dos pacotes na rede: https://github.com/Dsa-Terminal\n')
                print('pkg install [pkgname]      Instala pacotes')
                print('pkg uninstall [pkgname]    Desinstala pacotes')
                print('pkg update                 Atualiza versão instalada do Dsa Terminal')
            # Python
            elif cmd.startswith('python3'):
                system('cls')
                if cmd == 'python3':
                    system(fr'Python3\Scripts\python.exe')
                else:
                    cmd = cmd.replace('python3', '')
                    cmd = cmd.replace('python3 ', '')
                    if '-m' in cmd:
                        system(fr'Python3\Scripts\python.exe {cmd}')
                    else:
                        system(fr'Python3\Scripts\python.exe files\{cmd}')
                system('title Dsa Terminal')
            elif cmd.startswith('pip3'):
                cmd = cmd.replace('pip3 ', '')
                cmd = cmd.replace('pip3', '')
                system(rf'Python3\Scripts\pip.exe {cmd}')
            # cmd
            elif cmd == 'cmd':
                system('cls')
                system('cmd')
            # Instalando pacotes
            elif cmd.startswith('sudo pkg install'):
                cmd = cmd.replace('sudo ', '')
                cmd = cmd.replace(' ', '')
                password = getpass("[sudo] Palavra-passe do Dsa Terminal: ").strip()
                if password == key:
                    packge.pkg_install(cmd)
                else:
                    print('[sudo] Senha invalida!\n')
                continue
            # Instalando pacotes
            elif cmd.startswith('pkg install'):
                print('13: Erro (Permissão negada)!')
                continue
            # Clidev
            elif cmd == 'cli-http':
                while True:
                    cmd = input('\033[32m[~]\033[m ')
                    if cmd == 'exit':
                        break
                    elif cmd.startswith('http'):
                        cmd = cmd.replace('http ', '')
                        cmd = cmd.replace('http', '')
                        system(r'cls')
                        system(r'run\http_cli\http.exe')
                    elif cmd == 'clear':
                        system('cls')
                    else:
                        pass
            # Caminho
            elif cmd == 'pwd':
                print(pwd)
                continue
            # Desinstalando pacotes
            elif cmd.startswith('pkg uninstall'):
                print('13: Erro (Permissão negada)!')
                continue
            # Desinstalando pacotes
            elif cmd.startswith('sudo pkg uninstall'):
                password = getpass("[sudo] Palavra-passe do Dsa Terminal: ").strip()
                if password == key:
                    packge.pkg_uninstall(cmd)
                else:
                    print('[sudo] Senha invalida!\n')
                continue
            # Dsa Terminal e-ditor
            elif cmd.startswith('nano'):
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
            # Escrever na tela
            elif cmd.startswith('echo'):
                cmd = cmd.replace('echo ', '')
                cmd = cmd.replace('echo', '')
                cmd = cmd.replace('"', '')
                cmd = cmd.replace(r'\n', '\n')
                cmd = cmd.replace(r'\t', '\t')
                try:
                    cmd = cmd.replace(r'%myload%', myload)
                except:
                    cmd = cmd.replace('%myload%', 'Dados não encontrados')
                if cmd == '/?':
                    print('Echo: Listagem de parametros\n')
                    print(r'echo [mensagem[parametros de formatação]]')
                    print(r'\t                Tab')
                    print(r'\n                Quebra de linha')
                    print(r'%myload%          Valor definido')
                else:
                    print(cmd)
                continue
            # Executar shell script
            elif cmd.startswith('./'):
                cmd = cmd.replace('./', '')
                system(fr'bin\bash.exe /files/{cmd}')
            # Lnk
            elif cmd.startswith('lnk'):
                cmd = cmd.replace('lnk', '')
                cmd = cmd.replace('lnk ', '')
                if cmd == '':
                    system(rf'run\framework.exe')
                elif cmd == '--edit':
                     system(fr'usr\bin\nano.exe /run/index.html')
            # Ajuda manual
            elif cmd == 'help':
                print('Comando:              Funão:\n')
                print('echo [mensagem]       Escreve mensagens na tela')
                print('pkg [parametros]      Gerenciador de pacotes')
                print('nano [arquivo]        Dsa Terminal E-ditor')
                print('help                  Exibe ajuda')
                print('version               Exibe versão instalada')
                print('python3 [parametros]  Python v3.8.6...')
                print('lnk [parametros]      Framework')
                print("gitlocal              Local no GitHub.com (url)")
                print('pip3 [parametros]     Pip3 para Python env')
                print('./[script]            Executa script')
                print('cli-http              Console httpie Client')
                print('pwd                   Caminho do diretorio')
                print('mkdir [pasta]         Cria uma pasta')
                print('ssl                   SSL Controller')
                print('ifconfig              Exibe configurações de IP')
                print('set [options]         Difinindo variaveis seriais')
                print('task                  Exibe Tarefas do Dsa Terminal')
                print('exit                  Sai do Dsa Terminal')
            # Local na rede
            elif cmd == 'gitlocal':
                print('Github: https://github.com/Dsa-Terminal/Dsa-Terminal.git\n')
            # Esmaeçer
            elif cmd == '':
                for d in range(0, 1):
                    continue
                del d
            # Upload de dados "string"
            elif cmd.startswith('set'):
                cmd = cmd.replace('set ', '')
                cmd = cmd.replace('set', '')
                cmd = cmd.replace(r'\n', '\n')
                cmd = cmd.replace(r'\t', '\t')
                cmd = cmd.replace(r'"', '')
                if cmd == '= nil':
                    del myload
                    print('Registro deletado!')
                    continue
                else:
                    myload = cmd
                    continue
                    print('')
            # Sair do Dsa Terminal
            elif cmd == 'exit':
                auto_get_ProgressBar(0.01)
                break
            # Limpa a tela
            elif cmd == 'clear':
                system('cls')
                continue
            # Mostra versão do Dsa Terminal
            elif cmd == 'version':
                print(__version__)
                continue
            # Dsa Terminal Update
            elif cmd == 'pkg update':
                update()
                system('pause')
                break
            # Lua Linguagem
            elif cmd.startswith('lua'):
                cmd = cmd.replace('lua ', '')
                cmd = cmd.replace('lua', '')
                system('title lua for Dsa Terminal')
                system('cls')
                if cmd == '':
                    system(r'var\Lua\lua.exe')
                else:
                    system(fr'var\Lua\lua.exe \files\{cmd}lua')
                system('title Dsa terminal')
            # Api 
            elif cmd == 'apimon':
                system(r'run\sudo\apimon.exe')
                print('')
                continue
            elif cmd == 'env':
                system(r'run\env.exe')
                print('')
                continue
            # Node.js Server
            elif cmd == 'node':
                system('cls')
                system('title node.js for Dsa Terminal')
                system(r'var\node.exe')
                system('title Dsa terminal')
                continue
            # Dir classico
            elif cmd.startswith('dir'):
                system(fr'bin\dir.exe {pwd}')
                continue
            # Criar diretorio
            elif cmd.startswith('mkdir'):
                cmd = cmd.replace('mkdir ', '')
                cmd = cmd.replace('mkdir', '')
                if cmd == '':
                    pass
                else:
                    system(fr'mkdir files\{cmd}')
                print('')
                continue
            # Tarefas
            elif cmd == 'task':
                print('Tarefas sendo executadas no sistema:')
                print('Nome do Serviço:       Local:                   Status:')
                print('______________________________________________________________________________')
                print('Host da Janela         [Serviço do Windows]     Executando...')
                print('Config.                /Terminal.exe            Executando...')
                print('Bash.exe               /bin/bash.exe            Executando...')
                print('Servições do http-cli  /run/http_cli/http.exe   Executando em segundo plano...')
                print('Github connection      /.git     <dir>          Executando...')
                print('Linux Subsystem        /Terminal.exe            Executando em segundo plano...')
                print('Gerenciador de Tarefas /Terminal.exe            Executando em segundo plano...')
                print('mingw64                /mingw64/Main.sh         Executando...')
                print('Phoenix Setup CMOS     /run/SetupUltility/...   Executando em segundo plano...')
                print('==============================================================================\n')
            # Criar arquivo
            elif cmd.startswith('touch'):
                cmd = cmd.replace('touch ', '')
                cmd = cmd.replace('touch', '')
                if cmd == '':
                    open(r'files\Novo arquivo.txt', 'wt+')
                else:
                    open(fr'files\{cmd}', 'wt+')
                    print(f"Criando arquivos {cmd}..."), sleep(1)
                    auto_get_ProgressBar(0.03)
                    continue
            # Phoenix Setup Utility
            elif cmd == 'gui':
                auto_get_ProgressBar(0.01)
                system(r'run\SetupUltility\PhoenixSetupGUI.exe')
                break
            # Remover...
            elif 'rm' in cmd:
                cmd = cmd.replace('rm ', '')
                cmd = cmd.replace('rm', '')
                if cmd == '':
                    print('Remove: Insira um nome-de-arquivo')
                else:
                    system(fr'del {pwd}\{cmd}')
                print('')
            # Listar de diretorios e objetos
            elif cmd == 'ls':
                system(rf'run\ls.exe {pwd}')
                print('')
                continue
            # Listagem de diretorios, objetos e ocultos
            elif cmd == 'ls -a':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                system(rf'run\ls {pwd} -a')
                print('')
                continue
            # Configurações de IP 
            elif cmd == 'ifconfig':
                print(f'Configuração de IP do Dsa Terminal [conexão direta]!')
                print(f'IP: [{ip}] Porta: [{porta}]')
                print(f'Rota de Gateway: {route} (Padrão)')
                continue
            # Apps e modulos do Dsa Terminal
            elif cmd == 'kernel':
                try:
                    startfile('Lib\kernel\main.exe')
                except FileNotFoundError:
                    print('Modulo não instalado no sistema do Dsa Terminal!')
                    print('Tente:')
                    print('      sudo pkg install kernel')
                continue
            # iPXE
            elif cmd == 'ipxe':
                i = iPXE()
                if i == False:
                    break
                else:
                    continue
            # Comando invalido!
            else:
                print(f'{cmd}: comando invalido!')
                continue
        except:
            i = iPXE()
            if i == False:
                break
            else:
                continue
# Senha invalida
elif start == None:
    print('\n\nSenha invalida\nPXE MOF: Exiting PXE ROM'), sleep(5.8)
    system('pause')
# Falhar Exiting Pxe Rom
else:
    system('cls')
    print('Error: No Botable Device')
    print("Don't have a installed System on Dsa Terminal as Device Operative")
    print('PXE MOF: Exiting iPxe Rom...'), sleep(6.26)
    auto_get_ProgressBar(0.001)
