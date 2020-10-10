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
__version__ = '1.0.7.2'
# Importando modulos
import socket
from os import system, startfile, mkdir, listdir
from random import randint
from time import strftime, sleep
from rich.console import Console
from rich.markdown import Markdown
from tqdm import tqdm, trange
from rich.progress import track
from bs4 import BeautifulSoup
from requests import get
# ==========================
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
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
    print('Lendo pacotes de https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(21)
    auto_get_ProgressBar(0.1)
    print('\033[mDecodificando Setups paea o Compilador GitBoster (info).'), sleep(1.99)
    ProgressBar('Validando Serial')
    system('bin\git.exe pull')
    print(f'Setup de versão {__version__} Anterior <==== Update selected')
    return True
# Configuração do atualizador
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
        cmd = command.replace('pkg uninstall ', '')
        print(f'Recolhendo informações do pacote {cmd}...'), sleep(5.25)
        ProgressBar('Desinstalando')
        system(fr'del Lib\{cmd}')
        return True
    def pkg_update(command):
        cmd = command.replace('pkg uninstall ', '')
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

    def __init__():
        pass
# Ping network Servidor
class ping:
    def __init__(self, ip_to_conect, porta_to_conect):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.03)
        try:
            s.connect_ex((ip_to_conect, int(porta_to_conect)))
        except:
            print('Ping: Erro ao tentar se conectar com o servidor!')
        else:
            print(f'Ping: Conectado com IP: [{ip_to_conect}] Porta: [{porta_to_conect}]!'), sleep(2.08)
            while True:
                try:
                    print('Ping: Recebendo respostas do Servidor....')
                    print('Ping: Diagnosticando dados seriais recebidos')
                    print('Ping: Matendo solicitação infinita de Socket (ipv4/tcp)')
                except KeyboardInterrupt:
                    break
    def __server__(self, listen):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.listen(int(listen))
        s.bind((ip, porta))
        while True:
            s.accept()
            print('Ping: Uma conexão recebida neste Servidor!')
            try:
                msg = 'Servidor: Bem-vindo, você esta conectado com o servidor!'
                s.send(msg.decode('utf-8'))
            except:
                continue
            msg = 'Servidor: Mais um nodo recebido!'
            s.send(msg.encode('utf-8'))
# Noticias da Web
class webnews:
    def __init__(self):
        pass
    def scrapping():
        site = get("https://news.google.com/rss?need=pt_br&gl=BR&hl=pt-BR&ceid=BR:pt-419")
        noticias = BeautifulSoup(site.text, 'html.parser')
        for item in noticias.findAll('item')[:5]:
            print(f'{item.title.text}')
    def covid_cases():
        site = get('https://covid19-brazil-api.now.sh/api/report/v1')
        casos = site.json()
        caso = casos['data'][14]['cases']
        suspeitos = casos['data'][14]['suspects']
        mortes = casos['data'][14]['deaths']
        print(f"Casos de covid-19: Agora existem {caso} casos de Covid em seu estado, com {suspeitos} casos \nsuspeitos e {mortes} mortes")
# Inicalizar
def __init__():
    system('cls')
    system('title Dsa Terminal -i --login --bin\init.sh')
    system('pause')
    if files.ArquivoExiste(fr'boot\boot.ini'):
        if files.ArquivoExiste(rf'boot\init.sh'):
            system(r'bin\bash.exe boot\init.sh')
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
    system('title Dsa Terminal')
    print(strftime('Iniciando Dsa Terminal...'))
    print(strftime(f'(C) %Y Dsa Terminal versão {__version__} Sessão: [{session}]'))
    print(strftime('====================Dsa Terminal========================')), sleep(2.9)
    while True:
        try:
            cmd: str = input(f'\033[32mroot@mainFrame20:~$\033[m ').strip()
            # Listagem de parametros do Pkg
            if cmd == 'pkg /?':
                print('Pkg: Listagem de parametros')
                print('Local dos pacotes na rede: https://github.com/Dsa-Terminal\n')
                print('pkg install [pkgname]      Instala pacotes')
                print('pkg uninstall [pkgname]    Desinstala pacotes')
                print('pkg update                 Atualiza versão instalada do Dsa Terminal')
            # Debug
            elif cmd == 'debug':
                system(r'mingw64\bin\edit_text.exe')
                continue
            # OpenSSL
            elif cmd == 'ssl':
                system(r'mingw64\bin\openssl.exe')
                continue
            # Instalando pacotes
            elif cmd.startswith('pkg install'):
                packge.pkg_install(cmd)
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
                        if cmd == '':
                            system('run\http_cli\http.exe')
                        else:
                            system(f'run\http_cli\http.exe {cmd}')
                    elif cmd == 'clear':
                        system('cls')
            # Desinstalando pacotes
            elif cmd.startswith('pkg uninstall'):
                packge.pkg_uninstall(cmd)
                continue
            # Listagem de parametros do WebNews
            elif cmd == 'wn /?':
                print('WebNews: Listagem de parametros\n')
                print('wn -g / --get       Machetes diarias')
                print('wn -c / --covid     Casos de Coronaviros no estado')
            # Noticias diarias
            elif cmd == 'wn -g' or cmd == 'wn --get':
                webnews.scrapping()
                continue
            # Casos de covid
            elif cmd == 'wn -c' or cmd == 'wn --covid':
                webnews.covid_cases()
                continue
            # Escutar portas
            elif cmd.startswith('ping -nc'):
                cmd = cmd.replace('ping -nc ', '')
                cmd = cmd.replace('ping -nc', '')
                if cmd == '':
                    print('Ping: É necessario fornecer uma porta!')
                else:
                    ping.nc(int(cmd))
            # Localhost Web Pages
            elif cmd == 'localhost':
                system('run\Main.exe')
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
                print(cmd)
                continue
            # Linha comentada
            elif cmd.startswith(';;'):
                auto_get_ProgressBar(0.01)
                continue
            # Localhost WebAr Server
            elif cmd == 'localhost':
                system(r'run\Main.exe')
                continue
            # Listagem de parametros do "echo "
            elif cmd == 'echo /?':
                print('Echo: Listagem de parametros\n')
                print(r'    echo [mensagem[parametros de formatação]]')
                print(r'\t                Tab')
                print(r'\n                Quebra de linha')
                print(r'%myload%          Valor definido')
            # Executar shell script
            elif cmd.startswith('./'):
                cmd = cmd.replace('./', '')
                system(fr'bin\bash.exe /files/{cmd}')
            # Ajuda manual
            elif cmd == 'help':
                print('Comando:              Funão:\n')
                print('echo [mensagem]       Escreve mensagens na tela')
                print('pkg [parametros]      Gerenciador de pacotes')
                print('nano [arquivo]        Dsa Terminal E-ditor')
                print('ping [parametros]     Opçõeses de rede remota')
                print('help                  Exibe ajuda')
                print('version               Exibe versão instalada')
                print('./[shell script]      Executa shell script')
                print('block                 Protetor de tela')
                print('localhost             Web Localhost')
                print('cli-http              Console httpie Client')
                print('wn [parametros]       Noticias da web')
                print('st [Tarefa]           Começa uma tarefa do Windows')
                print('mkdir [pasta]         Cria uma pasta')
                print('ifconfig              Exibe configurações de IP')
                print('set [options]         Difinindo variaveis seriais')
                print('task                  Gerenciador de Tarefas')
                print('touch [arquivo]       Cria um arquivo')
                print('incluide [modulo]     Importa modulo e o executa')
                print('exit                  Sai do Dsa Terminal')
            # Protetor de tela
            elif cmd == 'block':
                startfile('Bubbles.scr')
                continue
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
            # Sair do Dsa Terminal
            elif cmd == 'exit':
                auto_get_ProgressBar(0.01)
                break
            # Limpa a tela
            elif cmd == 'clear':
                system('cls')
                continue
            # Limpa a tela
            elif cmd == 'cls':
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
                    system('var\Lua\lua.exe')
                else:
                    system(f'var\Lua\lua.exe {cmd}')
                system('title Dsa terminal')
            # Node.js Server
            elif cmd == 'node':
                system('cls')
                system('title node.js for Dsa Terminal')
                system(r'var\node.exe')
                system('title Dsa terminal')
                continue
            # Criar diretorio
            elif cmd.startswith('mkdir'):
                cmd = cmd.replace('mkdir ', '')
                cmd = cmd.replace('mkdir', '')
                if cmd == '':
                    pass
                else:
                    system(fr'mkdir files\{cmd}')
                continue
            # Tarefas
            elif cmd == 'task':
                print('Tarefas sendo executadas no sistema:')
                print('Nome do Serviço:       Local:                   Status:')
                print('Host da Janela         [Serviço do Windows]     Executando...')
                print('Config.                /Terminal.exe            Executando...')
                print('Bash.exe               /bin/bash.exe            Executando...')
                print('Serviçõs do http-cli   /run/http_cli/http.exe   Executando em segundo plano...')
                print('Github connection      /.git     <dir>          Executando...')
                print('Linux Subsystem        /Terminal.exe            Executando em segundo plano...')
                print('Gerenciador de Tarefas /Terminal.exe            Executando em segundo plano...')
                print('mingw64                /mingw64/Main.sh         Executando...')
                print('Phoenix Setup CMOS     /run/SetupUltility/...   Executando em segundo plano...')
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
                    system(fr'del files\{cmd}')
            # Listar de diretorios e objetos
            elif cmd == 'ls':
                system(r'bin\bash.exe bin\listdir.sh')
                print('')
                continue
            # Listagem de diretorios, objetos e ocultos
            elif cmd == 'ls -a':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                system(r'bin\bash.exe bin\listall.sh')
                print('')
                continue
            # Abrir Paginas da Web
            elif cmd.startswith('web'):
                cmd = cmd.replace('web ', '')
                cmd = cmd.replace('web', '')
                system(f'start "" "https://{cmd}"')
                auto_get_ProgressBar(0.01)
                del http
            # Configurações de IP 
            elif cmd == 'ifconfig':
                print('Configuração de IP do Dsa Terminal [conexão direta]!')
                print(f'IP: [{ip}] Porta: [80]')
                continue
            # Incluir e executar Modulo
            elif cmd.startswith('incluide'):
                cmd = cmd.replace('incluide ', '')
                cmd = cmd.replace('incluide', '')
                if cmd == '':
                    print('Incluide: Modulo sem nome')
                else:
                    auto_get_ProgressBar(0.01)
                    system(fr'Lib\{cmd}\Main.exe')
            # Comando invalido!
            else:
                print(f'{cmd}: comando invalido!')
                continue
        except:
            continue
# Falhar Exiting Pxe Rom
else:
    system('cls')
    print('Error: No Botable Device')
    print("Don't have a installed System on Dsa Terminal as Device Operative")
    print('Exiting iPxe Rom...'), sleep(6.26)
    auto_get_ProgressBar(0.001)
