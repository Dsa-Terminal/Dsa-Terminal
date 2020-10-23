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
__version__ = '1.8.2'
# Importando modulos
import socket
from os import system, startfile, mkdir, listdir, remove
from random import randint, choice
from time import strftime, sleep
from getpass import getpass
from tqdm import tqdm, trange
from rich.progress import track
from requests import get
# Variaveis globais
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
route = 'net-1: 10.0.0.155/255.255.255.0 gw 10.0.0.1'
path = ['/bin', '/usr/bin', '/var', '/var/Lua', '/run',
        '/run/sudo', '/run/http_cli', '/run/SetupUltility',
        '/Python3/Scripts', '/dev', '/cmd', '/Lib', '/Lib/dpkg',
        '/mingw64', '/mingw64/ssl', '/mingw64/libexec/gti-core',
        '/boot', '/boot/drivers', 'var/node_modules/npm', '/tmp',
        'usr/etc', '/usr/lib', '/usr', '/usr/share']
assoc = {
    '.exe': 'executavel', '.py': 'python file',
    '.com': 'executavel', '.run': 'executavel',
    '.api': 'api de módulo', 'packge.json': 'node.js server',
    '.lua': 'lua script', '.js': 'javascipt file',
    '.sc': 'arquivo em lotes do Dsa Terminal',
    '.txt': 'arquivo de texto', '.exc': 'arquivo de texto',
    '.html': 'documento web', '.xml': 'documento xml'
}
run = r'Dsa Terminal -i --login --boot\boot.ini'
session = randint(0, 291462)
pwd = "/files"
porta = 82
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
    pass
def auto_get_ProgressBar(time):
    for step in track(range(100)):
        do_step(step, time)
def update():
    system('title [Update] - Dsa Terminal')
    print('Lendo pacotes de https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(2.8)
    auto_get_ProgressBar(0.1)
    print('\033[mDecodificando Setups para o Compilador GitBoster (info).'), sleep(1.99)
    ProgressBar('Validando Serial')
    system('bin\git.exe pull')
    print(f'Setup de versão {__version__} Anterior <==== Update selected')
    return True
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
    def pkg_search(appname):
        print('Lote:       Nome do pacote:        Versão:     Tag:           ')
        print('______________________________________________________________')
        if appname == 'kernel':
            print('@tool-boot  kernel                 v0.0.1      #Servicodeerro')
            print('@devtools   kernel-tool         Não disponivel  #Ferramentas')
        elif appname == 'ssh':
            print('@ping(more) ssh                    v1.8.3      #Conectividade')
        else:
            print('            ---Nenhum pacote encontrado---')
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
        system('ping')
        return True
    def connect(self, ip):
        system(f'ping -t {ip}')
        return True
def virtualenv(env_name):
    print(f'Criando ambiente virtual {env_name}...'), sleep(1.22)
    try:
        mkdir(fr'files\{env_name}')
    except FileExistsError:
        print('Venv: Esta pasta já existe!')
    else:
        print('Movendo arquivos base para o ambiente de desenvolvimento...'), sleep(13.162)
        print('Finalizando...\nDando toques finais...\nExecutando Venv...')
        print('Terminado tudo. . .', end=''), sleep(12)
        print('criado!!!')
        print()
def iPXE():
    system('cls')
    print('iPXE -- Open Source Network Boot Firmware -- http://ipxe.org')
    print('Features: HTTP iSCSI DNS TFTP AoE FCoE TFTP COMBOOT ELF PXE PXEXT\n'), sleep(9.2)
    while True:
        cmd: str = input('iPXE> ')
        if cmd == 'route':
            print(route)
        elif cmd == 'sanboot' or cmd == run:
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
def matrixe(AF_INET):
    chars_to_print = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', ' ']
    hall = True
    for c in range(0, AF_INET):
        try:
            for i in range(100):
                print(choice(chars_to_print), end='', sep='')
            print(i)
        except KeyboardInterrupt:
            break
    print('\n')
def __init__():
    system(r'cls')
    run = r'Dsa Terminal -i --login --boot\boot.ini'
    system('pause')
    if files.ArquivoExiste('boot\drivers\IMPOSSIBLE-BOOT-BIOSTOPXEROM.ipxe'):
        return run, ''
    else:
        system(f'title {run}')
        if files.ArquivoExiste(fr'boot\boot.ini'):
            if files.ArquivoExiste(rf'boot\init.sh'):
                if files.ArquivoExiste(r'boot\drivers\pass.exc'):
                    with open(r'boot\drivers\pass.exc', 'rt') as key:
                        key = key.read()
                        password = getpass('Password: ').strip()
                        if password == key:
                            try:
                                with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'rt') as commit:
                                    commit = commit.read()
                            except FileNotFoundError:
                                pass
                            else:
                                print('Iniciando depuração do sistema....'), sleep(10.8)
                                remove('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db')
                                print('Tentando manter instabilidade na inicialização...'), sleep(12)
                                input('Pressione ENTER para continuar a depuração. . .')
                                system('timeout /T 10')
                                print('Retomando o Shell Kernel para erros potenciais...')
                                print('Seja paciente, a depuração pode demorar horas'), sleep(12.837)
                                print('_______________________________________________________\n')
                                print('Carregando modulos de entrada... ', end=''), sleep(10)
                                print('carregado!!!')
                                print('\n\n')
                                print('Checando Framework de serviço do Node.JS Server...'), sleep(1.287)
                                print('Zerando cache para melhor instabilidade...'), sleep(19.37)
                                auto_get_ProgressBar(0.001)
                                ProgressBar('Iniciando')
                                print('Iniciando o Dsa Terminal...'), sleep(18)
                            system('cls')
                            return run, True
                        elif password == f'{key} --main':
                            password = password.replace(f'{key} --main', '')
                            run = input('Boot Code:\>_').strip()
                            if run == r'Dsa Terminal -i --login --boot\boot.ini':
                                try:
                                    with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'rt') as commit:
                                        commit = commit.read()
                                except FileNotFoundError:
                                    pass
                                else:
                                    print('Iniciando depuração do sistema....'), sleep(10.8)
                                    remove('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db')
                                    print('Tentando manter instabilidade na inicialização...'), sleep(12)
                                    input('Pressione ENTER para continuar a depuração. . .')
                                    system('timeout /T 10')
                                    print('Retomando o Shell Kernel para erros potenciais...')
                                    print('Seja paciente, a depuração pode demorar horas'), sleep(12.837)
                                    print('_______________________________________________________\n')
                                    print('Carregando modulos de entrada... ', end=''), sleep(10)
                                    print('carregado!!!')
                                    print('\n\n')
                                    print('Checando Framework de serviço do Node.JS Server...'), sleep(1.287)
                                    print('Zerando cache para melhor instabilidade...'), sleep(19.37)
                                    auto_get_ProgressBar(0.001)
                                    ProgressBar('Iniciando')
                                    print('Iniciando o Dsa Terminal...'), sleep(18)
                                return run, True
                            elif run == r'Dsa Terminal -i --login --bin\boot.ini --nocache':
                                try:
                                    with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'rt') as commit:
                                        commit = commit.read()
                                except FileNotFoundError:
                                    pass
                                else:
                                    print('Iniciando depuração do sistema....'), sleep(10.8)
                                    remove('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db')
                                    print('Tentando manter instabilidade na inicialização...'), sleep(12)
                                    input('Pressione ENTER para continuar a depuração. . .')
                                    system('timeout /T 10')
                                    print('Retomando o Shell Kernel para erros potenciais...')
                                    print('Seja paciente, a depuração pode demorar horas'), sleep(12.837)
                                    print('_______________________________________________________\n')
                                    print('Carregando modulos de entrada... ', end=''), sleep(10)
                                    print('carregado!!!')
                                    print('\n\n')
                                    print('Checando Framework de serviço do Node.JS Server...'), sleep(1.287)
                                    print('Zerando cache para melhor instabilidade...'), sleep(19.37)
                                    auto_get_ProgressBar(0.001)
                                    ProgressBar('Iniciando')
                                    print('Iniciando o Dsa Terminal...'), sleep(18)
                                return run, True
                            else:
                                system(f'title {run}')
                                return run, False
                        elif password == f'{key} --network':
                            password = password.replace(f'{key} --network', '')
                            cmd: str = input('Boot Image in ServerLocal: ').strip().lower()
                            try:
                                run = get(cmd)
                            except:
                                print(f'Config.: Não encontrei nenhuma imagem de boot em {cmd}!')
                                return run, False
                            else:
                                print(run)
                                system('pause')
                                return run, True
                else:
                    print('Registre uma palavra-passe para o Dsa Terminal!\n')
                    while True:
                        password = getpass('Password: ').strip()
                        if password == '':
                            print('Config.: Insira uma palavra-passe!')
                        elif password == 'abc123' or password == 'ABC123':
                            print('Config.: Pó meu, capricha na senha mano!')
                        else:
                            with open(r'boot\drivers\pass.exc', 'wt+') as key:
                                files.Write(r'boot\drivers\pass.exc', password)
                                system('cls')
                                break
                    return run, True
            else:
                return run, 'hmbdxyt'
        else:
            return run, 'ffcffff'
# Setup
run, start = __init__()
if start == True:
    with open(r'boot\drivers\pass.exc', 'rt') as key:
        key = key.read()
    system('cls')
    system('title Dsa Terminal')
    print(strftime('Iniciando Dsa Terminal...'))
    print(strftime(f'(C) %Y Dsa Terminal v{__version__} Sessão: [{session}]'))
    print(strftime('===================Dsa Terminal==============')), sleep(0.08)
    while True:
        try:
            system(f'echo ┌─────────[\033[32m%username%@%computername%\033[m] \033[34m~\033[m')
            cmd: str = input(f'└─$ ').strip()
            if cmd == 'pkg /?':
                print('Pkg: Listagem de parametros')
                print('Local dos pacotes na rede: https://github.com/Dsa-Terminal\n')
                print('pkg install [pkgname]      Instala pacotes')
                print('pkg uninstall [pkgname]    Desinstala pacotes')
                print('pkg search [pkgname]       Procura um pacote')
                print('pkg update                 Atualiza versão instalada do Dsa Terminal')
            elif cmd.startswith('pkg search'):
                cmd = cmd.replace('pkg search ', '')
                cmd = cmd.replace('pkg search', '')
                if cmd == '':
                    print('Pkg: Insira-um-nome-de-pacote!')
                else:
                    packge.pkg_search(appname=cmd)
            elif cmd.startswith('python3'):
                system('cls')
                if cmd == 'python3':
                    system(fr'Python3\Scripts\python.exe')
                    continue
                else:
                    cmd = cmd.replace('python3', '')
                    cmd = cmd.replace('python3 ', '')
                    if '-m' in cmd:
                        system(fr'Python3\Scripts\python.exe {cmd}')
                    else:
                        system(fr'Python3\Scripts\python.exe files\{cmd}')
                system('title Dsa Terminal')
            elif cmd.startswith('pip'):
                cmd = cmd.replace('pip ', '')
                cmd = cmd.replace('pip', '')
                system(rf'Python3\Scripts\pip.exe {cmd}')
            elif cmd == 'sudo' or cmd == 'pkg':
                print('Config.: Insira parametros')
                continue
            elif cmd.startswith('sudo pkg install'):
                cmd = cmd.replace('sudo ', '')
                cmd = cmd.replace(' ', '')
                password = getpass("[sudo] Palavra-passe do Dsa Terminal: ").strip()
                if password == key:
                    packge.pkg_install(cmd)
                else:
                    print('[sudo] Senha invalida!\n')
                continue
            elif cmd.startswith('pkg install'):
                print('13: Erro (Permissão negada)!')
                continue
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
                        continue
                    else:
                        pass
            elif cmd == 'pwd':
                print(pwd)
                continue
            elif cmd.startswith('pkg uninstall'):
                print('13: Erro (Permissão negada)!')
                continue
            elif cmd.startswith('sudo pkg uninstall'):
                password = getpass("[sudo] Palavra-passe do Dsa Terminal: ").strip()
                if password == key:
                    packge.pkg_uninstall(cmd)
                else:
                    print('[sudo] Senha invalida!\n')
                continue
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
            elif cmd.startswith('echo'):
                cmd = cmd.replace('echo ', '')
                cmd = cmd.replace('echo', '')
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
            elif cmd.startswith('./'):
                cmd = cmd.replace('./', '')
                system(fr'bin\bash.exe /files/{cmd}')
            elif cmd.startswith('lnk'):
                cmd = cmd.replace('lnk', '')
                cmd = cmd.replace('lnk ', '')
                if cmd == '':
                    system(rf'run\framework.exe')
                elif cmd == ' --edit':
                    system(fr'usr\bin\nano.exe /run/index.html')
                elif cmd == '--edit':
                    system(fr'usr\bin\nano.exe /run/index.html')
            elif cmd == r'Dsa Terminal -i --login --boot\boot.ini':
                system('cls')
                system('title Dsa Terminal')
                print(strftime('Iniciando Dsa Terminal...'))
                print(strftime(f'(C) %Y Dsa Terminal v{__version__} Sessão: [{session}]'))
                print(strftime('===================Dsa Terminal==============')), sleep(0.08)
            elif cmd == r'Dsa Terminal -i --login --boot\boot.ini --nocache':
                system('cls')
                system('title Dsa Terminal')
                print(strftime('Iniciando Dsa Terminal...'))
                print(strftime(f'(C) %Y Dsa Terminal v{__version__} Sessão: [{session}]'))
                print(strftime('===================Dsa Terminal==============')), sleep(0.08)
            elif cmd == 'help':
                print('Comando:             Fução:')
                print('_____________________________________________________')
                print('echo [mensagem]      Escreve mensagens na tela')
                print('pkg [parametros]     Gerenciador de pacotes')
                print('nano [arquivo]       Dsa Terminal E-ditor')
                print('help                 Exibe ajuda')
                print('version              Exibe versão instalada')
                print('python3 [parametros] Python v3.8.6...')
                print('lnk [parametros]     Framework')
                print('gui                  Phoenix Setup Utility')
                print("gitlocal             Local no GitHub.com (url)")
                print('pip [parametros]     Gerenciador de pacotes do Config.')
                print('./[script]           Executa script')
                print('wmic                 Sistema de Alias')
                print('prompt               Suspende o console')
                print('firefox              Inicia o firefox')
                print('issue                Relatar um poblema')
                print('cli-http             Console httpie Client')
                print('pwd                  Caminho do diretorio')
                print('mkdir [pasta]        Cria uma pasta')
                print('ssl                  SSL Controller')
                print('touch [arquivo]      Criar arquivo')
                print('ifconfig             Exibe configurações de IP')
                print('set [parametros]     Difinindo variaveis seriais')
                print('task                 Exibe Tarefas do Dsa Terminal')
                print('exit                 Sai do Dsa Terminal')
            elif cmd == 'issue':
                system('mingw64\gh.exe issue create')
                continue
            elif cmd == 'gitlocal':
                print('Github: https://github.com/Dsa-Terminal/Dsa-Terminal.git\n')
                continue
            elif cmd == 'cmatrix':
                matrixe(127363846129649436438972987436743)
                continue
            elif cmd == '':
                for d in range(0, 1):
                    continue
                del d
            elif cmd.startswith('virtualenv'):
                cmd = cmd.replace('virtualenv', '')
                cmd = cmd.replace('virtualenv ', '')
                if cmd == '':
                    print('Venv: Insira-um-nome-de-ambiente-virtual!')
                else:
                    virtualenv(cmd)
            elif cmd == 'prompt':
                system('pause')
                cpntinue
            elif cmd.startswith('set'):
                cmd = cmd.replace('set ', '')
                cmd = cmd.replace('set', '')
                cmd = cmd.replace(r'\n', '\n')
                cmd = cmd.replace(r'\t', '\t')
                cmd = cmd.replace(r'"', '')
                if cmd == '= nil':
                    try:
                        del myload
                        del loaded
                    except:
                        print('Config.: Nenhum registro salvo!')
                    else:
                        print('Config.: Registro deletado!')
                    continue
                else:
                    myload = cmd
                    loaded = True
                    continue
                    print('')
            elif cmd == 'exit':
                auto_get_ProgressBar(0.01)
                break
            elif cmd == 'clear':
                system('cls')
                continue
            elif cmd == 'version':
                print(strftime(f'Dsa Terminal Copyright (C) %Y v{__version__}'))
                continue
            elif cmd == 'pkg update':
                update()
                system('pause')
                break
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
            elif cmd == 'apimon':
                system(r'run\sudo\apimon.exe')
                print('')
                continue
            elif cmd == 'cls':
                system('cls')
                continue
            elif cmd == 'env':
                system(r'run\env.exe')
                print('')
                continue
            elif cmd == 'wmic':
                print('')
                system('wmic')
                continue
            elif cmd == 'firefox':
                system(r'start network\firefox\firefox.exe')
                print('')
                continue
            elif cmd == 'node':
                system('cls')
                system('title node.js for Dsa Terminal')
                system(r'var\node.exe')
                system('title Dsa terminal')
                continue
            elif cmd.startswith('dir'):
                system(fr'bin\dir.exe {pwd}')
                continue
            elif cmd.startswith('mkdir'):
                cmd = cmd.replace('mkdir ', '')
                cmd = cmd.replace('mkdir', '')
                if cmd == '':
                    pass
                else:
                    system(fr'mkdir files\{cmd}')
                print('')
                continue
            elif cmd == 'task':
                print('Tarefas sendo executadas:')
                print('Nome do Serviço:       Local:                   Status:')
                print('______________________________________________________________________________')
                try:
                    cmd = loaded
                    if cmd == True:
                        print('String Sync            /Terminal.exe            Executando...')
                except:
                    pass
                print('')
                print('Tarefas do Sistema:')
                print('______________________________________________________________________________')
                print('Host da Janela         [Serviço do Windows]     Executando...')
                print('Config.                /Terminal.exe            Executando...')
                print('Bash.exe               /bin/bash.exe            Executando...')
                print('Catalogo de Serviço    /ipxe.sc                 Executando primariamente...')
                print('Servições do http-cli  /run/http_cli/http.exe   Executando em segundo plano...')
                print('Github connection      /.git     <dir>          Executando...')
                print('Linux Subsystem        /Terminal.exe            Executando em segundo plano...')
                print('Gerenciador de Tarefas /Terminal.exe            Executando em segundo plano...')
                print('mingw64                /mingw64/Main.sh         Executando...')
                print('Phoenix Setup CMOS     /run/SetupUltility/...   Executando em segundo plano...')
                print('==============================================================================\n')
            elif cmd.startswith('touch'):
                cmd = cmd.replace('touch ', '')
                cmd = cmd.replace('touch', '')
                if cmd == '':
                    open(r'files\Novo arquivo.txt', 'wt+')
                else:
                    open(fr'files\{cmd}', 'wt+')
                    print(f"Criando arquivo {cmd}..."), sleep(1)
                    auto_get_ProgressBar(0.03)
                    continue
            elif cmd == 'gui':
                auto_get_ProgressBar(0.01)
                system(r'start run\SetupUltility\PhoenixSetupGUI.exe')
                break
            elif 'rm' in cmd:
                cmd = cmd.replace('rm ', '')
                cmd = cmd.replace('rm', '')
                if cmd == '':
                    print('Remove: Insira um nome-de-arquivo')
                else:
                    system(fr'del {pwd}\{cmd}')
                print('')
            elif cmd == 'ls':
                system(rf'run\ls.exe {pwd}')
                print('')
                continue
            elif cmd == 'ls -a':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                system(rf'run\ls {pwd} -a')
                print('')
                continue
            elif cmd == 'ifconfig':
                print(f'Configuração de IP do Dsa Terminal [conexão direta]!')
                print(f'IP: [{ip}] Porta: [{porta}]')
                print(f'Rota de Gateway: {route} (Padrão)')
                continue
            elif cmd == 'kernel':
                try:
                    system('Lib\kernel\main.exe')
                except FileNotFoundError:
                    print('Modulo não instalado no sistema do Dsa Terminal!')
                    print('Tente:')
                    print('      sudo pkg install kernel')
                continue
            elif cmd == 'ipxe':
                i = iPXE()
                if i == False:
                    with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'wt+') as commit:
                        commit = commit.read()
                    break
                else:
                    continue
            else:
                print(f'{cmd}: comando invalido!')
                continue
        except:
            i = iPXE()
            if i == False:
                with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'wt+') as commit:
                    commit = commit.read()
                break
            else:
                continue
elif start == None:
    print('\n\nSenha invalida\nPXE MOF: Exiting PXE ROM'), sleep(5.8)
    system('pause')
elif start == False:
    print('Config.: Módulo de inicianlização não recebeu comando valido para inicializar o Dsa Terminal!')
    print('PXE MOF: Exiting PXE ROM...'), sleep(6.26)
    a = open('boot\drivers\IMPOSSIBLE-BOOT-BIOSTOPXEROM.ipxe', 'wt+')
elif start == '':
    print('Config.: Ha um poblema impedindo a inicialização do Dsa Terminal!')
    coregir = input('Você dejesa executar o depurador[S,N]? ').upper()
    if coregir == 'S':
        print('')
        system('timeout /T 10')
        print('Iniciando depuração do sistema...'), sleep(2.37)
        remove('boot\drivers\IMPOSSIBLE-BOOT-BIOSTOPXEROM.ipxe')
        print('Terminando Depuração...', end=''), sleep(16.9)
        print('concluida!!!')
        print('\nPXE MOF: Exiting PXE ROM...'), sleep(6.26)
    elif coregir == 'N':
        print('\nPXE MOF: Exiting PXE ROM...'), sleep(6.26)
    else:
        print('\nConfig.: Isso não é uma opção!')
        print('PXE MOF: Exiting PXE ROM...'), sleep(6.26)
else:
    system('cls')
    print('Error: No Botable Device')
    print("Don't have a installed System on Dsa Terminal as Device Operative")
    print('PXE MOF: Exiting PXE ROM...'), sleep(6.26)
    auto_get_ProgressBar(0.001)
