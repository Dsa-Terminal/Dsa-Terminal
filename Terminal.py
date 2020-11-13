# Dsa Terminal codigo-fonte
__version__ = f'1.9.0' # Versão do Dsa Terminal
__license__ = f'(C) 2020 Dsa Software Fundation [Mit License]' # Licença atualizada da dsa Software Fundation
# Metodo de entrada serial
if __name__ == "__main__":
    # Inicializar com toda força
    try:
        from flask import Flask
        import pygame, asyncio, sqlite3, sys, platform, socket
        from os import system, startfile, mkdir, listdir, remove, path, chdir
        from random import randint, choice
        from time import strftime, sleep
        from getpass import getpass
        from tqdm import tqdm, trange
        from rich.progress import track
        from requests import get
    # Erro na importação
    except:
        # Importando modulos do Python
        from time import sleep
        from os import system
        from platform import platform
        # Reparo automatico
        system('cls')
        print('Iniciando o Dsa Terminal. . .'), sleep(7.37)
        print('Caregando dados do Reparo Automatico do Dsa Terminal. . .'), sleep(12)
        if platform().startswith('Windows'):
            system("cls")
            print(f"Config.: Erro ao inicializar o Dsa Terminal v{__version__}")
            print(r'Opções de inicializição avançada:')
            print(f'1 - CMD                                     2 - Instalar dependencias do Python')
            print(r'3 - Tentar iniciar o Dsa Terminal novamente 4 - Diagnosticar erro')
            print(f'5 - Abrir Github                            6 - Sair')
            print('')
            while True:
                cmd = input('Code:\>_').strip()
                if cmd == '1':
                    system('cls')
                    system('cmd')
                    system('cls')
                    print('Iniciando o Dsa Terminal. . .'), sleep(7.37)
                    print('Caregando dados do Reparo Automatico do Dsa Terminal. . .'), sleep(12)
                    system("cls")
                    print(f"Config.: Erro ao inicializar o Dsa Terminal v{__version__}")
                    print(r'Opções de inicializição avançada:')
                    print(f'1 - CMD                                     2 - Instalar dependencias do Python')
                    print(r'3 - Tentar iniciar o Dsa Terminal novamente 4 - Diagnosticar erro')
                    print(f'5 - Abrir Github                            6 - Sair')
                elif cmd == '2':
                    system('pip3 install pygame')
                    system('pip3 install sqlite3')
                    system('pip3 install tqdm')
                    system('pip3 install rich')
                    system('pip3 install flask')
                elif cmd == '3':
                    while True:
                        system('cls')
                        print('=====================================================')
                        print('Inicializar o:')
                        print('1 - Terminal.exe')
                        print('2 - python3 Terminal.py')
                        print('-----------------------------------------------------')
                        cmd = input('>>> ').strip()
                        if cmd == '1':
                            system("start Terminal.exe")
                            break
                        elif cmd == '2':
                            system('start Terminal.py')
                            break
                        else:
                            print('Isso não é uma opção')
                            print('')
                    break
                elif cmd == '4':
                    print('Procurando poblemas. . .'), sleep(12)
                    if files.ArquivoExiste('boot\Boot.py'):
                        if files.ArquivoExiste(r'boot\boot.ini'):
                            if files.ArquivoExiste(r'boot\Boot.tar.gz'):
                                if files.ArquivoExiste('boot\efi.exe'):
                                    if path.exists(r'bin\bash.exe'):
                                        pass
                                    else:
                                        print('Config.: Não existe um bash para operar')
                                else:
                                    print('Config.: Não existe a base do depurador e inciaizador')
                            else:
                                print('Config.: Não existe um arquivo base para extair drivers')
                        else:
                            print('Config.: Não existe uma configuração para o depurador do Config.')
                    else:
                        print('Config.: Não existe um arquivo base para o Boot')
                    print("O Config. não encontrou as dependencias")
                elif cmd == '5':
                    system('start "" "https:/github.com/Dsa-Terminal/Dsa-Terminal/issue"')
                    continue
                elif cmd == '6':
                    print('Deletando variaveis. . .'), sleep(10)
                    print('PXE MOF: Exiting PXE ROM'), sleep(5)
                    break
        else:
            print(f"Config.: Erro ao inicializar o Dsa Terminal v{__version__}")
            print('Config.: O Dsa Terminal só pode ser iniciado em Windows')
    # Inicializando
    else:
        # Variaveis globais
        ip = socket.gethostbyname(socket.gethostname())
        conn = sqlite3.connect("Config.db").cursor()
        route = choice(['net-1: 10.0.0.155/255.255.255.0 gw 10.0.0.1', 'net-2: 17.0.0.192/255.255.255.0 gw 10.0.0.2',
                       'net-3: 10.0.0.255/255.255.255.0 gw 10.0.0.4', 'net-4: 17.0.0.174/255.255.255.0 gw 10.0.0.3'])
        app = Flask(__name__)
        pwd = "/files" # Diretorio atual
        win_pwd = r'\files' # Diretorio atual no windows 10
        # Barra de progresso tradicional
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
        # Configurações da barra de progresso padrão
        def do_step(set, time):
            sleep(time)
            pass
        # Barra de progresso padrão
        def auto_get_ProgressBar(time, title="Carregando..."):
            for step in track(range(100), description=title):
                do_step(step, time)
        # Kernel de atualizações
        def update():
            system('title [Update] - Dsa Terminal')
            print('Lendo pacotes de https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(0.01)
            print('Git 1: https://github.com/Dsa-Terminal/Dsa-Terminal/releases....'), sleep(0.023)
            print('Git 2: https://github.com/Dsa-Terminal/Dsa-Terminal/commit/22af2ee0b1d92e9b3ebe909d5371324e0ee717e2...'), sleep(1)
            print('[Trabalhando em atualizações]...', end=''), sleep(2.934)
            print('Concluido!!')
            print('Git 3: https://github.com/Dsa-Terminal/Dsa-Terminal/releases/ [Processando...]'), sleep(0.02)
            system('bin\git.exe pull')
            system('title Dsa Terminal')
            return True
        # Gerenciador de pacotes padrão
        class packge:
            def __init__(self):
                pass
            # Instalar pacotes
            def pkg_install(command):
                cmd = command.replace('pkginstall ', '')
                cmd = command.replace('pkginstall', '')
                if cmd == '':
                    print('Pkg: Insira-um-nome-de-pacote-valido\n')
                elif cmd == 'Dsa-Terminal':
                    print('Pkg: Para atualizar o Dsa Terminal você deve usar o comando "pkg update"\n')
                else:
                    print(f'Lendo coleção https://github.com/Dsa-Terminal/{cmd}...'), sleep(0.01)
                    print(f'Git 1: [Downloading...] https://github.com/Dsa-Terminal/{cmd}/releases/download/{cmd}-master.zip'), sleep(1)
                    auto_get_ProgressBar(0.001, title="downloading...")
                    print(f'Git 2: https://github.com/Dsa-Terminal/{cmd}/commit/22af2ee0b1e9b3ebe909d5371324e0ee717e2...'), sleep(1.92)
                    print(f'Git 3: [Making Dependences...][Building Setup.exe].....'), sleep(0.002)
                    system(fr'bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}.git')
                    system(fr'move {cmd} Lib')
                    return True
            # Procurar pacotes
            def pkg_search(appname):
                print('Lote:       Nome do pacote:        Versão:     Tag:           ')
                print('______________________________________________________________')
                if appname == 'kernel-tool':
                    print('@devtools   kernel-tool         Não disponivel  #Ferramentas')
                elif appname == 'kernel':
                    print('@tool-boot    kernel               v0.0.1      #Servicodeerro')
                    print('@devtools   kernel-tool         Não disponivel  #Ferramentas')
                elif appname == 'ssh':
                    print('@ping(more)     ssh                v1.8.3      #Conectividade')
                else:
                    print('            ---Nenhum pacote encontrado---')
            # Desinstalar pacotes
            def pkg_uninstall(command):
                cmd = command.replace('pkg uninstall ', '')
                print(f'Recolhendo informações do pacote {cmd}...'), sleep(5.25)
                ProgressBar('Desinstalando')
                system(fr'del Lib\{cmd}')
                return True
            # Atualizar pacotes
            def pkg_update(command):
                cmd = command.replace('pkg update ', '')
                print(f'\033[32mLendo coleção https://github.com/Dsa-Terminal/{cmd}...'), sleep(8)
                print(f'Acessando archive do Dsa Terminal [{cmd}.git]'), sleep(4)
                auto_get_ProgressBar(1, title='uninstalling...')
                ProgressBar('Baixando tools')
                system(rf'del Lib\{cmd}')
                system(fr'bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}.git')
                system(fr'move {cmd} Lib')
                return True
        # Gerenciador de Arquivos
        class files:
            def __init__(self):
                pass
            # Escrever em um arquivo
            def Write(filename, texto):
                try:
                    a = open(filename, 'wt')
                except FileNotFoundError:
                    return False
                else:
                    a.write(texto)
                    a.close()
            # Criar um arquivo
            def CriarArquivo(filename):
                try:
                    a = open(filename, 'wt+')
                    a.close()
                except Exception as e:
                    return False
                else:
                    return True
            # Verificar se um determinado arquivo existe
            def ArquivoExiste(filename):
                try:
                    a = open(filename, 'rt')
                except FileNotFoundError:
                    return False
                else:
                    return True
        # iPXE Network System
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
                    mixer('Startup.mp3')
                    print(strftime('Iniciando Dsa Terminal...'))
                    print(strftime(f'(C) %Y Dsa Terminal v{__version__} | IP: [{ip}]'))
                    print(strftime('===================Dsa Terminal===================')), sleep(0.08)
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
        # Escrevedo pelo cmd
        def println(msg):
            system(f'echo {msg}')
            return True
        # FrameWork
        @app.route('/')
        def main_route():
            site = '''
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Dsa Terminal Framework</title>
            </head>
            <body>
                <h1>Hello, World!<h1>
                <script>
                    var cmd = window.prompt("Código")
                </script>
            </body>
            </html>
            '''
            return site
        # Nome do host local
        def host():
            return socket.gethostname()
        # Dsa Terminal
        if platform.platform().startswith('Windows'):
            # Driver de inicialização
            def __init__():
                if files.ArquivoExiste('boot\Boot.py'):
                    if files.ArquivoExiste(r'boot\boot.ini'):
                        if files.ArquivoExiste(r'boot\Boot.tar.gz'):
                            if files.ArquivoExiste('boot\efi.exe'):
                                if path.exists(r'bin\bash.exe'):
                                    try:
                                        a = open('boot\drivers\pass.exc', 'rt').read()
                                    except FileNotFoundError:
                                        print(f'Seja bem vindo Dsa Terminal v{__version__}!')
                                        print(f'Para iniciar crie uma senha forte para o Dsa Terminal, ela não precisa ser a mesma do Windows')
                                        password = getpass("Registre uma palavra-passe: ")
                                        files.CriarArquivo('boot\drivers\pass.exc')
                                        files.Write('boot\drivers\pass.exc', password)
                                        return True
                                    else:
                                        return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            start = __init__()
            # Inicializar normalmente
            if start == True:
                # Driver de som
                pygame.mixer.init()
                def mixer(sound):
                    pygame.mixer.music.load(fr'sample\rootfs\{sound}')
                    pygame.mixer.music.play()
                # Descobrindo a senha
                with open(r'boot\drivers\pass.exc', 'rt') as key:
                    key = key.read()
                # Inicializando o Terminal
                system('cls')
                mixer('Startup.mp3')
                system('title Dsa Terminal')
                protocol = "MINGW64"
                print(strftime('Iniciando Dsa Terminal...'))
                print(strftime(f'(C) %Y Dsa Terminal v{__version__} | IP: [{ip}]'))
                print(strftime('===================Dsa Terminal===================')), sleep(0.08)
                # Sistema de armazenamento de logs
                timeout = strftime(f'(C) %Y Dsa Terminal v{__version__} | IP: [{ip}] | Computador: [{host()}]\n')
                if files.ArquivoExiste('tmp\Booted.log'):
                    files.Write('tmp\Boted.log', timeout)
                    pass
                elif not files.ArquivoExiste('tmp\Booted.log'):
                    files.CriarArquivo('tmp\Boted.log')
                    files.Write('tmp\Boted.log', timeout)
                # Laço infinito
                while True:
                    # Tentar Fazer
                    try:
                        # Prompt de Comando
                        println(f'┌─────────[\033[32m%username%@{host()}\033[m] \033[35m{protocol}\033[m \033[34m{pwd}\033[m')
                        cmd: str = input(f'└─$ ').strip()
                        # MSYS Protocol CMDs
                        if protocol == 'MSYS':
                            # Mundando protocolo
                            if cmd == 'mingw64':
                                protocol = 'MINGW64'
                                print()
                                continue
                            # Bash as Sudo's
                            elif cmd == 'bash':
                                password = getpass('[sudo] Palavra-passe do Dsa Terminal: ').strip()
                                if key == password:
                                    system('cls')
                                    system('title SUDO: /usr/bin/bash.exe')
                                    system(r'usr\bin\bash.exe')
                                    system('cls')
                                else:
                                    print('[sudo] Senha invalida!\n')
                                system('title Dsa Terminal')
                                continue
                            # Interface de linha de comando "http cliente"
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
                            # Nome do host atual
                            elif cmd == 'hostname':
                                system(r'usr\bin\hostname.exe')
                                print('')
                            # Dsa Terminal E-ditor
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
                            # Imprimir mensagem na tela
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
                            # Framework DevServer
                            elif cmd == 'lnk':
                                try:
                                    app.run()
                                except:
                                    continue
                                continue
                            # Sistema de Alias
                            elif cmd == 'wmic':
                                print('')
                                system('wmic')
                                continue
                            # Deviced
                            elif cmd == 'tty':
                                system(r'usr\bin\tty.exe')
                                continue
                            # Deletar arquivos e diretorios
                            elif 'rm' in cmd:
                                cmd = cmd.replace('rm ', '')
                                cmd = cmd.replace('rm', '')
                                if cmd == '':
                                    print('Remove: Insira um nome-de-arquivo')
                                else:
                                    system(fr'del {win_pwd}\{cmd}')
                                print('')
                            # Listar diretorios e objetos
                            elif cmd.startswith('ls'):
                                cmd = cmd.replace('ls', '')
                                cmd = cmd.replace('ls ', '')
                                system(rf'run\ls.exe {pwd} {cmd}')
                                print('')
                                continue
                            # Configurações de rede
                            elif cmd == 'ifconfig':
                                print(f'Configuração de IP do Dsa Terminal [conexão direta]!')
                                print(f'IP: [{ip}] Porta: [22]')
                                print(f'Gateway: {route}')
                                print(f'=====================================================')
                                continue
                            # PHP para Dsa Terminal
                            elif cmd.startswith('php'):
                                cmd = cmd.replace('php ', '')
                                cmd = cmd.replace('php', '')
                                system(f'var\php\php.exe {cmd}')
                                continue
                            # Se entrada for vazia
                            elif cmd == '':
                                print('')
                                continue
                            # Gerenciar o sistema de arquivos na rede
                            elif cmd.startswith('psftp'):
                                system('sbin\psftp.exe')
                                print('')
                                continue
                            # Criar arquivo
                            elif cmd.startswith('touch'):
                                cmd = cmd.replace('touch ', '')
                                cmd = cmd.replace('touch', '')
                                if cmd == '':
                                    open(fr'{pwd}\Novo arquivo.txt', 'wt+')
                                else:
                                    try:
                                        file = open(fr'{pwd}\{cmd}', 'wt+')
                                    except FileExistsError:
                                        print('Config.: Já existe um arquivo com este nome')
                                    else:
                                        print('Config.: Criando Arquivo. . .', end=''), sleep(2)
                                        print('criado!!!')
                                        while True:
                                            try:
                                                alinar: str = str(input(''))
                                                files.Write(fr'{pwd}\{cmd}', alinar)
                                            except:
                                                break
                                    continue
                            # Sair deste protocolo
                            elif cmd == 'exit':
                                protocol = 'MINGW64'
                                print('')
                            # Putty
                            elif cmd == 'putty':
                                startfile('sbin\putty.exe')
                                continue
                            # NetCat Builder
                            elif cmd.startswith('ncat'):
                                cmd = cmd.replace('ncat ', '')
                                cmd = cmd.replace('ncat', '')
                                try:
                                    system(fr'sample\ncat.exe {cmd}')
                                except:
                                    continue
                                continue
                            # Limpar a tela
                            elif cmd == 'clear':
                                system('cls')
                                continue
                            # Ajuda
                            elif cmd == 'help':
                                print("Listagem de comandos do Protocolo MSYS:")
                                print('Comando:             Descrição:')
                                print('_____________________________________________________')
                                print('cli-http             Console httpie Client')
                                print('hostname             Nome do host atual')
                                print('nano [arquivo]       Dsa Terminal E-ditor')
                                print('echo [mensagem]      Escreve mensagens na tela')
                                print('lnk                  Framework')
                                print('wmic                 Sistema de Alias')
                                print('tty                  Device connectado')
                                print('ifconfig             Exibe configurações de IP')
                                print("php                  PHP iNTERPRET")
                                print("psftp                Conexão remota")
                                print("touch [arquivo]      Criar arquivo")
                                print('putty                Putty driver')
                                print('ncat [parametros]    NetCat Driver de rede')
                                print('clear                Limpa a tela')
                                print('exit                 Sai deste Protocolo')
                            # Comando invalido
                            else:
                                print(f'{cmd}: comando não encontrado!')
                                print('')
                                continue
                        # Protocolo padrão
                        if protocol == 'MINGW64':
                            # Mundança de protocolo
                            if cmd == 'msys':
                                protocol = 'MSYS'
                                print('')
                                continue
                            # Python 2.7.18
                            elif cmd.startswith('python'):
                                cmd = cmd.replace('python ', '')
                                cmd = cmd.replace('python', '')
                                system(rf'usr\local\Python27\python.exe {win_pwd}\{cmd}')
                            # Pip do python2
                            elif cmd.startswith('pip'):
                                cmd = cmd.replace('pip ', '')
                                cmd = cmd.replace('pip', '')
                                system(fr'usr\local\Python27\Scripts\pip.exe {cmd}')
                            # Ajuda do "PKG"
                            elif cmd == 'pkg /?' or cmd == 'pkg':
                                print('Pkg: Listagem de parametros')
                                print('Local dos pacotes na rede: https://github.com/Dsa-Terminal\n')
                                print('pkg install [pkgname]      Instala pacotes')
                                print('pkg uninstall [pkgname]    Desinstala pacotes')
                                print('pkg search [pkgname]       Procura um pacote')
                                print('pkg update                 Atualiza versão instalada do Dsa Terminal')
                            # Procurar pacotes. . .
                            elif cmd.startswith('pkg search'):
                                cmd = cmd.replace('pkg search ', '')
                                cmd = cmd.replace('pkg search', '')
                                if cmd == '':
                                    print('Pkg: Insira-um-nome-de-pacote!')
                                else:
                                    packge.pkg_search(appname=cmd)
                            # Python 3.8.6
                            elif cmd.startswith('python3'):
                                if cmd == 'python3':
                                    system(fr'Python3\Scripts\python.exe')
                                    continue
                                else:
                                    cmd = cmd.replace('python3', '')
                                    cmd = cmd.replace('python3 ', '')
                                    if '-m' in cmd:
                                        system(fr'Python3\Scripts\python.exe {cmd}')
                                    else:
                                        system(fr'Python3\Scripts\python.exe {win_pwd}\{cmd}')
                                system('title Dsa Terminal')
                            # /Python3/Scripts/pip.exe
                            elif cmd.startswith('pip3'):
                                cmd = cmd.replace('pip3 ', '')
                                cmd = cmd.replace('pip3', '')
                                system(rf'Python3\Scripts\pip.exe {cmd}')
                            # Bash as Sudo's
                            elif cmd == 'sudo su':
                                password = getpass('[sudo] Palavra-passe do Dsa Terminal: ').strip()
                                if key == password:
                                    system('cls')
                                    system('title SUDO: /usr/bin/bash.exe')
                                    system(r'usr\bin\bash.exe')
                                    system('cls')
                                else:
                                    print('[sudo] Senha invalida!\n')
                                system('title Dsa Terminal')
                                continue
                            # Banner do Dsa Terminal
                            elif cmd == 'bunner':
                                print('######   ######   ####        ####### ###### #####  #### ####  º  ##    #  ####  #')
                                print('#     #  #       #    #          #    #      #    # #  # #  #  #  # #   # #    # #')
                                print('#     #  ######  #    #          #    ###    #####  #   #   #  #  #  #  # #    # #')
                                print('#     #        # ######          #    #      #    # #       #  #  #   # # ###### #')
                                print('######   ######  #    #          #    ###### #    # #       #  #  #    ## #    # #####')
                            # Ajuda do sudo
                            elif cmd == 'sudo':
                                print('Usage: sudo [commmand] <parameters>')
                                print('')
                                print(' commands:')
                                print('     pkg install         Install Packges With Root permission')
                                print('    pkg uninstall       Uninstall Packges WIth Root permission')
                                print('')
                                print(' parameters:')
                                print('     --version      -v      Print sudo version istalled')
                                print("      --help        -h      Print Sudo's help")
                                print('      --unix                Print Unix Sudo in WSL')
                            elif cmd == 'sudo --help' or cmd == 'sudo -h':
                                print('Usage: sudo [commmand] <parameters>')
                                print(' ')
                                print(' commands:')
                                print('     pkg install         Install Packges With Root permission')
                                print('    pkg uninstall       Uninstall Packges WIth Root permission')
                                print('')
                                print(' parameters:')
                                print('     --version      -v      Print sudo version istalled')
                                print("      --help        -h          Print Sudo's help")
                                print('      --unix                  Print Unix Sudo in WSL')
                            # Versão do sudo
                            elif cmd == 'sudo --version' or cmd == 'sudo -v':
                                print('Dsa Terminal @Root_User v0.0.2020.1')
                                println(rf'root@{host()}')
                            # Nome do host atual
                            elif cmd == 'hostname':
                                system(r'usr\bin\hostname.exe')
                                print('')
                            # Intalando pacotes com permissão de adiministrador
                            elif cmd.startswith('sudo pkg install'):
                                cmd = cmd.replace('sudo ', '')
                                cmd = cmd.replace(' ', '')
                                password = getpass("[sudo] Palavra-passe do Dsa Terminal: ").strip()
                                if password == key:
                                    packge.pkg_install(cmd)
                                else:
                                    print('[sudo] Senha invalida!\n')
                                continue
                            # Intalando pacotes
                            elif cmd.startswith('pkg install'):
                                print('13: Erro (Permissão negada)!')
                                continue
                            # VLC Media Player
                            elif cmd == 'vlc':
                                system(r'start run\MediaPlayer\vlc.exe')
                                continue
                            # Interface de linha de comando "http cliente"
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
                            # Navegando pelos dirs
                            elif cmd.startswith('cd'):
                                cmd = cmd.replace('cd ', '')
                                cmd = cmd.replace('cd', '')
                                if cmd == '..':
                                    chdir(fr'{win_pwd}\{cmd}')
                                try:
                                    chdir(fr'{win_pwd}\{cmd}')
                                except:
                                    print('Config.: Não foi possivel encontrar o diretorio')
                                else:
                                    pwd = fr'{pwd}/{cmd}'
                                    win_pwd = rf'{win_pwd}\{cmd}'
                                print('')
                            # Diretorio atual
                            elif cmd == 'pwd':
                                print(pwd)
                                continue
                            # Desinstalando pacotes
                            elif cmd.startswith('pkg uninstall'):
                                print('13: Erro (Permissão negada)!')
                                continue
                            # Desinstalando pacotes com permissão de adiministrador
                            elif cmd.startswith('sudo pkg uninstall'):
                                password = getpass("[sudo] Palavra-passe do Dsa Terminal: ").strip()
                                if password == key:
                                    packge.pkg_uninstall(cmd)
                                else:
                                    print('[sudo] Senha invalida!\n')
                                continue
                            # Dsa Terminal E-ditor
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
                            # Imprimir mensagem na tela
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
                            # Executar
                            elif cmd.startswith('./'):
                                cmd = cmd.replace('./', '')
                                if cmd == 'vlc':
                                    system(r'start run\MediaPlayer\vlc.exe')
                                    print("")
                                    continue
                                elif cmd == 'putty':
                                    startfile('sbin\putty.exe')
                                    print('')
                                elif cmd == 'firefox':
                                    system(r'start network\firefox\firefox.exe')
                                    print('')
                                    continue
                                else:
                                    if cmd.endswith('.sh'):
                                        system(fr'bin\bash.exe {pwd}/{cmd}')
                                    elif cmd.endswith('.exe'):
                                        system(rf'{pwd}/{cmd}')
                                    elif cmd.endswith('.py'):
                                        system(rf'Python3\Scripts\python.exe {win_pwd}\{cmd}')
                                    elif cmd.endswith('.lua'):
                                        system(fr'var\Lua\lua.exe {win_pwd}\{cmd}')
                            # Framework DevServer
                            elif cmd == 'lnk':
                                try:
                                    app.run()
                                except:
                                    continue
                                continue
                            # Notas de versão
                            elif cmd == 'changelog':
                                with open('CHANGELOG.TXT') as logme:
                                    print(logme.read())
                            # Arduino IDE
                            elif cmd == 'arduino':
                                startfile(r'var\Arduino\arduino.exe')
                                continue
                            # Driver de audio
                            elif cmd.startswith('drv -m --sound"'):
                                if cmd.endswith('"'):
                                    cmd = cmd.replace('drv -m --sound', '')
                                    cmd = cmd.replace('"', '')
                                    if cmd == '':
                                        print('Driver de Audio: Insira-um-nome-de-arquivo')
                                    else:
                                        try:
                                            pygame.mixer.music.load(fr'{win_pwd}\{cmd}')
                                            pygame.mixer.music.play()
                                        except Exception as e:
                                            print('Driver de Audio: Erro na reprodução do arquivo')
                                            print(e)
                            # Ajuda maxima
                            elif cmd == 'help':
                                print("Listagem de comandos do Protocolo MINGW64:")
                                print('Comando:             Descrição:')
                                print('_____________________________________________________')
                                print('echo [mensagem]      Escreve mensagens na tela')
                                print('pkg [parametros]     Gerenciador de pacotes')
                                print('nano [arquivo]       Dsa Terminal E-ditor')
                                print('ncat [parametros]    NetCat driver de rede')
                                print('help                 Exibe ajuda')
                                print('tty                  Device connectado')
                                print('hostname             Nome do host atual')
                                print('mintty               Mintty Console usr/bin/mintty.exe')
                                print('version              Exibe versão instalada')
                                print('python3 [parametros] Python v3.8.6...')
                                print('ls [parametros]      Lista diretorios e objetos')
                                print('dir [parametros]     Lista o que tem no diretorio')
                                print('lnk                  Framework')
                                print('gui                  Phoenix Setup Utility')
                                print("gitlocal             Local no GitHub.com (url)")
                                print('pip [parametros]     Gerenciador de pacotes do Config.')
                                print('pip3 [parametros]    Gerenciador de pacotes do Config.')
                                print('./[script or app]    Executar')
                                print('prompt               Suspende o console')
                                print('firefox              Inicia o firefox')
                                print('issue                Relatar um poblema')
                                print('cli-http             Console httpie Client')
                                print('pwd                  Caminho do diretorio')
                                print('mkdir [pasta]        Cria uma pasta')
                                print('rm [dirs/files]      Deletar algo')
                                print('touch [arquivo]      Criar arquivo')
                                print('ifconfig             Exibe configurações de IP')
                                print('set [parametros]     Difinindo variaveis seriais')
                                print('task                 Exibe Tarefas do Dsa Terminal')
                                print('exit                 Sai do Dsa Terminal')
                            # Criar poblema no repositorio do GitHub
                            elif cmd == 'issue':
                                system('mingw64\gh.exe issue create')
                                continue
                            # NetCat Builder
                            elif cmd.startswith('ncat'):
                                cmd = cmd.replace('ncat ', '')
                                cmd = cmd.replace('ncat', '')
                                try:
                                    system(fr'sample\ncat.exe {cmd}')
                                except:
                                    continue
                                continue
                            # GIT URL local
                            elif cmd == 'gitlocal':
                                print('Github: https://github.com/Dsa-Terminal/Dsa-Terminal.git\n')
                                continue
                            # Alarme
                            elif cmd == 'alone':
                                mixer('Alarm01.wav')
                                print('')
                            # Se entrada for vazia
                            elif cmd == '':
                                print('')
                                continue
                            # Suspuender console
                            elif cmd == 'prompt':
                                print('')
                                system('pause')
                                continue
                            # Armazenar cadeia de caracteres variavel
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
                            # Finalizar sessão
                            elif cmd == 'exit':
                                print('Encerrando Tarefas. . .'), sleep(2.3)
                                auto_get_ProgressBar(0, title="Saindo...")
                                break
                            # Limpar a tela
                            elif cmd == 'clear':
                                system('cls')
                                continue
                            # Exibir versão do Dsa Terminal
                            elif cmd == 'version':
                                print(strftime(f'Dsa Terminal Copyright (C) %Y v{__version__}'))
                                continue
                            # Atualizar o Dsa Terminal
                            elif cmd == 'pkg update':
                                update()
                                continue
                            # Lua Linguagem interpret
                            elif cmd.startswith('lua'):
                                cmd = cmd.replace('lua ', '')
                                cmd = cmd.replace('lua', '')
                                system('title lua for Dsa Terminal')
                                system('cls')
                                if cmd == '':
                                    system(r'var\Lua\lua.exe')
                                else:
                                    system(fr'var\Lua\lua.exe {win_pwd}\{cmd}lua')
                                system('title Dsa terminal')
                            # Api de troca e montagem no Aplicativo. . .
                            elif cmd == 'apimon':
                                system(r'start run\sudo\apimon.exe')
                                print('')
                                continue
                            # Limpar a tela
                            elif cmd == 'cls':
                                system('cls')
                                continue
                            # Sistema binario de controle
                            elif cmd == 'env':
                                system(r'start run\env.exe')
                                print('')
                                continue
                            # FireFox para Dsa Terminal
                            elif cmd == 'firefox':
                                system(r'start network\firefox\firefox.exe')
                                print('')
                                continue
                            # Node.js Server para Dsa Terminal
                            elif cmd == 'node':
                                system('cls')
                                system('title node.js for Dsa Terminal')
                                system(r'var\node.exe')
                                system('title Dsa terminal')
                                continue
                            # Arquitetura do Sistema
                            elif cmd == 'arch':
                                system(r'usr\bin\arch.exe')
                                continue
                            # Id do controlador
                            elif cmd == 'id':
                                system(r'usr\bin\id.exe')
                                continue
                            # Bash and Shell
                            elif cmd == 'mintty':
                                startfile(r'usr\bin\mintty.exe')
                                continue
                            # Data
                            elif cmd == 'date':
                                system(r'usr\bin\date.exe')
                                print('')
                                continue
                            # Gimp setup
                            elif cmd == 'gpg':
                                system(r'usr\bin\gpg.exe')
                                continue
                            # LICENSE
                            elif cmd == 'license':
                                with open('LICENSE') as lic:
                                    print(lic.read())
                            # Exibe diretorios e arquivos
                            elif cmd.startswith('dir'):
                                system(fr'usr\bin\dir.exe {pwd}')
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
                            # Exibe tarefas sendo executadas
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
                            # Deviced
                            elif cmd == 'tty':
                                system(r'usr\bin\tty.exe')
                                continue
                            # Gerenciar o sistema de arquivos na rede
                            elif cmd.startswith('psftp'):
                                system('sbin\psftp.exe')
                                print('')
                                continue
                            # Criar arquivo
                            elif cmd.startswith('touch'):
                                cmd = cmd.replace('touch ', '')
                                cmd = cmd.replace('touch', '')
                                if cmd == '':
                                    open(fr'{pwd}\Novo arquivo.txt', 'wt+')
                                else:
                                    try:
                                        file = open(fr'{pwd}\{cmd}', 'wt+')
                                    except FileExistsError:
                                        print('Config.: Já existe um arquivo com este nome')
                                    else:
                                        print('Config.: Criando Arquivo. . .', end=''), sleep(2)
                                        print('criado!!!')
                                        while True:
                                            try:
                                                alinar: str = str(input(''))
                                                files.Write(fr'{pwd}\{cmd}', alinar)
                                            except:
                                                break
                                    continue
                            # Phoenix Setup Gui TrustedBios (tm) CMOS Utility
                            elif cmd == 'gui':
                                auto_get_ProgressBar(0.01)
                                system(r'start run\SetupUltility\PhoenixSetupGUI.exe')
                                break
                            # Deletar arquivos e diretorios
                            elif 'rm' in cmd:
                                cmd = cmd.replace('rm ', '')
                                cmd = cmd.replace('rm', '')
                                if cmd == '':
                                    print('Remove: Insira um nome-de-arquivo')
                                else:
                                    system(fr'del {win_pwd}\{cmd}')
                                print('')
                            # Listar diretorios e objetos
                            elif cmd.startswith('ls'):
                                cmd = cmd.replace('ls', '')
                                cmd = cmd.replace('ls ', '')
                                system(rf'run\ls.exe {pwd} {cmd}')
                                print('')
                                continue
                            # Configurações de rede
                            elif cmd == 'ifconfig':
                                print(f'Configuração de IP do Dsa Terminal [conexão direta]!')
                                print(f'IP: [{ip}] Porta: [22]')
                                print(f'Gateway: {route}')
                                print(f'=====================================================')
                                continue
                            # PHP para Dsa Terminal
                            elif cmd.startswith('php'):
                                cmd = cmd.replace('php ', '')
                                cmd = cmd.replace('php', '')
                                system(f'var\php\php.exe {cmd}')
                                continue
                            # API de erro "Kernel"
                            elif cmd == 'kernel':
                                try:
                                    startfile('Lib\kernel\main.exe')
                                except FileNotFoundError:
                                    print('Modulo não instalado no sistema do Dsa Terminal!')
                                    print('Tente:')
                                    print('      sudo pkg install kernel')
                                continue
                            # API de rede "secure Shell"
                            elif cmd == 'ssh':
                                try:
                                    startfile('Lib\ssh\ssh.exe')
                                except FileNotFoundError:
                                    print('Modulo não instalado no sistema do Dsa Terminal!')
                                    print('Tente:')
                                    print('      sudo pkg install ssh')
                            # iPXE LAN COMBOOT Network
                            elif cmd == 'ipxe':
                                i = iPXE()
                                if i == False:
                                    with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'wt+') as commit:
                                        commit = commit.read()
                                    break
                                else:
                                    continue
                            # Comando invalido
                            else:
                                print(f'{cmd}: comando não encontrado!')
                                print('')
                                continue
                    # Interrupção pelo teclado
                    except KeyboardInterrupt:
                        i = iPXE()
                        if i == False:
                            with open('tmp\DEBUG-NEED-INSTART(Win32)-SYSTEMCTRL-LOADSYS.db', 'wt+') as commit:
                                commit = commit.read()
                            break
                        else:
                            continue
                    # Ocorreu algum erro
                    except Exception as erro:
                        system('cls')
                        for i in range(0, 5):
                            mixer('ERROR_Media.mp3')
                        print('\033[33mFatal:\033[m Dsa Terminal Excepition Interrupt')
                        print('Config.: Estamos coletando Iinformações sobre o e depois encerraremos esta sessão do Dsa Terminal para você!'), sleep(0.01)
                        sleep(0.111)
                        break
            # No Bootable DEVICE: Falha no Boot
            else:
                system('cls')
                mixer('ERROR_Media.mp3')
                print('Error: No Botable Device')
                print("Don't have a installed System on Dsa Terminal as Device Operative")
                print('PXE MOF: Exiting PXE ROM...'), sleep(6.26)
                auto_get_ProgressBar(0.001)
        else:
            print(f"Config.: Erro ao inicializar o Dsa Terminal v{__version__}")
            print('Config.: O Dsa Terminal só pode ser iniciado em Windows')
