# -*- coding: utf-8 -*-
__version__ = "1.9.0"
__license__ = "(C) 2020 Dsa Software Fundation [MIT LICENSE]"
if __name__ == "__main__":
    try:
        import pygame, asyncio, sqlite3, sys, platform, socket
        from os import system, startfile, mkdir, listdir, remove, path, chdir
        from random import randint, choice
        from time import strftime, sleep
        from getpass import getpass
        from rich.progress import track
        from requests import get
    except:
        # Importing modules
        from time import sleep
        from os import system
        from platform import platform
        # Auto repair
        system('cls')
        print('Starting Dsa Terminal. . .'), sleep(7.37)
        print('Loading datas for start Dsa Terminal auto repair. . .'), sleep(12)
        if platform().startswith('Windows'):
            system("cls")
            print(f"Config.: Start of Dsa Terminal v{__version__} was Falid\n")
            print(r'Avanced options:')
            print(f'1 - CMD                                     2 - Install dependences')
            print(r'3 - Try start Dsa Terminal newer            4 - Search error')
            print(f'5 - Open Github                             6 - Scapy')
            print(f'7 - Boot with GUI                           8 - Help')
            print(f'9 - Bash                                    10 - Restaur Dsa Terminal')
            print(f'11 - Shell                                  12 - Sair')
            while True:
                cmd = input('Code:\>_').strip()
                if cmd == '1':
                    system('cls')
                    system('cmd')
                    system("cls")
                    print(f"Config.: Start of Dsa Terminal v{__version__} was Falid\n")
                    print(r'Avanced options:')
                    print(f'1 - CMD                                     2 - Install dependences')
                    print(r'3 - Try start Dsa Terminal newer            4 - Search error')
                    print(f'5 - Open Github                             6 - Scapy')
                    print(f'7 - Boot with GUI                           8 - Help')
                    print(f'9 - Bash                                    10 - Restaur Dsa Terminal')
                    print(f'11 - Shell                                  12 - Sair')
                elif cmd == '2':
                    system('pip3 install pygame')
                    system('pip3 install sqlite3')
                    system('pip3 install rich')
                    system('pip3 install flask')
                elif cmd == '3':
                    while True:
                        system('cls')
                        print('=====================================================')
                        print('Start:')
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
                            print('This is not option ')
                            print('')
                    break
                elif cmd == '4':
                    print('Searching. . .'), sleep(12)
                    print('')
                elif cmd == '5':
                    system('start "" "https:/github.com/Dsa-Terminal/Dsa-Terminal"')
                    continue
                elif cmd == '6':
                    system('network\scapy.exe')
                    continue
                elif cmd == '7':
                    print('Installing tmp files...'), sleep(4)
                    print('loading usr/bin/env bash'), sleep(13)
                    system('start run\SetupUltility\PhoenixSetupGUI.exe')
                elif cmd == '8':
                    print(r'Avanced options:')
                    print(f'1 - CMD                                     2 - Install dependences')
                    print(r'3 - Try start Dsa Terminal newer            4 - Search error')
                    print(f'5 - Open Github                             6 - Scapy')
                    print(f'7 - Boot with GUI                           8 - Help')
                    print(f'9 - Bash                                    10 - Restaur Dsa Terminal')
                    print(f'11 - Shell                                  12 - Sair')
                elif cmd == '9':
                    system(r'bin\bash.exe')
                    continue
                elif cmd == '10':
                    print('Forcing Exit. . .'), sleep(4)
                    print("FATAL: No have operating system installed in Dsa Terminal!"), sleep(1000098765436789483765489087654098764589084279584572968547965421738999999999999999999999999999999999999999999999999.999)
                    break
                elif cmd == '11':
                    system('bin\sh.exe')
                    continue
                elif cmd == '12':
                    print('Unistaling talls and driver kernel. . .'), sleep(10)
                    print('PXE MOF: Exiting PXE ROM'), sleep(5)
                    break
        else:
            print(f"Config.: Dsa Terminal v{__version__} not was started sucefully")
            print('Config.: Dsa Terminal only started in Windows 10, sorry!')
    else:
        ip = socket.gethostbyname(socket.gethostname())
        conn = sqlite3.connect("Config.db").cursor()
        route = choice(['net-1: 10.0.0.155/255.255.255.0 gw 10.0.0.1', 'net-2: 17.0.0.192/255.255.255.0 gw 10.0.0.2',
                       'net-3: 10.0.0.255/255.255.255.0 gw 10.0.0.4', 'net-4: 17.0.0.174/255.255.255.0 gw 10.0.0.3'])
        pwd = "/home"
        win_pwd = r'\home'
        class BosterTrips:
            def __init__(self):
                return True

            def do_step(set, time):
                sleep(time)
                pass

            def ProgressBar(time, title="Loading..."):
                for step in track(range(100), description=title):
                    do_step(step, time)

            def __enter__(self):
                return True

            def update():
                system('title [Update] - Dsa Terminal')
                print('Reading packges: https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(0.01)
                print('Git 1: https://github.com/Dsa-Terminal/Dsa-Terminal/releases....'), sleep(0.023)
                print('Git 2: https://github.com/Dsa-Terminal/Dsa-Terminal/commit/22af2ee0b1d92e9b3ebe909d5371324e0ee717e2...'), sleep(1)
                print('[Working in updates]...', end=''), sleep(2.934)
                print('Finish!!')
                print('Git 3: https://github.com/Dsa-Terminal/Dsa-Terminal/releases/ [Updating...]'), sleep(0.02)
                system('bin\git.exe pull')
                system('title Dsa Terminal')
                return True

            class packge:
                def __init__(self):
                    pass
                def pkg_install(command):
                    cmd = command.replace('pkginstall ', '')
                    cmd = command.replace('pkginstall', '')
                    if cmd == '':
                        print('Pkg: Insert a packge name\n')
                    elif cmd == 'Dsa-Terminal':
                        print('Pkg: To update Dsa Terminal use command "pkg update"\n')
                    else:
                        print(f'Reading packges: https://github.com/Dsa-Terminal/{cmd}...'), sleep(0.01)
                        print(f'Git 1: [Downloading...] https://github.com/Dsa-Terminal/{cmd}/releases/download/{cmd}-master.zip'), sleep(1)
                        ProgressBar(0.001, title="downloading...")
                        print(f'Git 2: https://github.com/Dsa-Terminal/{cmd}/commit/22af2ee0b1e9b3ebe909d5371324e0ee717e2...'), sleep(1.92)
                        print(f'Git 3: [Making Dependences...][Building Setup.exe].....'), sleep(0.002)
                        system(fr'bin\git.exe clone https://github.com/Dsa-Terminal/{cmd}.git')
                        system(fr'move {cmd} Lib')
                        return True
                def pkg_search(appname):
                    print('Lote:       Nome do pacote:        Versão:     Tag:           ')
                    print('______________________________________________________________')
                    if appname == 'kernel-tool':
                        print('@devtools   kernel-tool           Indisponible  #Ferramentas')
                    elif appname == 'kernel':
                        print('@tool-boot    kernel               v0.0.1      #Servicodeerro')
                        print('@devtools   kernel-tool         Indisponible    #Ferramentas')
                    elif appname == 'ssh':
                        print('@ping(more)     ssh                v1.8.3       #Connection')
                    else:
                        print('            ---Packge not found---')
                def pkg_uninstall(command):
                    cmd = command.replace('pkg uninstall ', '')
                    print(f'Recolhendo informações do pacote {cmd}...'), sleep(5.25)
                    ProgressBar('Desinstalando')
                    system(fr'del Lib\{cmd}')
                    return True
                # Atualizar pacotes
                def pkg_update(command):
                    cmd = command.replace('pkg update', '')
                    print(f'Reading packges: https://github.com/Dsa-Terminal/{cmd}...'), sleep(8)
                    print(f'Connecting... Acess to [{cmd}.git]'), sleep(4)
                    auto_get_ProgressBar(1, title='Uninstalling...')
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

            def iPXE():
                system('cls')
                print('iPXE -- Open Source Network Boot Firmware -- http://ipxe.org')
                print('Features: HTTP iSCSI DNS TFTP AoE FCoE TFTP COMBOOT ELF PXE PXEXT\n'), sleep(1)
                while True:
                    cmd: str = input('iPXE> ')
                    if cmd == 'route':
                        print(route)
                    elif cmd == 'sanboot':
                        sleep(1)
                        system('cls')
                        mixer('Startup.mp3')
                        print(strftime('Starting Dsa Terminal...'))
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
                        sleep(5)
                        return False
                        break
                    elif cmd == 'ping':
                        print('iPXE: Your network Firmware connection is variable!')
                        print(f'iPXE: Network COMBOOT IP: {ip}\n')
                    else:
                        print(f'{cmd}: iPXE command not found!')
            
            def host():
                return socket.gethostname()
        def println(msg):
            system(f'echo {msg}')
            return True
        ftp = BosterTrips
        if platform.platform().startswith('Windows'):
            def __init__():
                if ftp.files.ArquivoExiste('boot\Boot.py'):
                    if ftp.files.ArquivoExiste(r'boot\boot.ini'):
                        if ftp.files.ArquivoExiste(r'boot\Boot.tar.gz'):
                            if ftp.files.ArquivoExiste('boot\efi.exe'):
                                if path.exists(r'bin\bash.exe'):
                                    try:
                                        a = open('boot\drivers\pass.exc', 'rt').read()
                                    except FileNotFoundError:
                                        print(f'Welcome to Dsa Terminal v{__version__}!')
                                        print(f"To start create an password [sudo]! The password don't need match with Windows password!")
                                        password = getpass("Registre uma palavra-passe: ")
                                        ftp.files.CriarArquivo('boot\drivers\pass.exc')
                                        ftp.files.Write('boot\drivers\pass.exc', password)
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
            if start == True:
                pygame.mixer.init()
                def mixer(sound):
                    pygame.mixer.music.load(fr'sample\rootfs\{sound}')
                    pygame.mixer.music.play()
                with open(r'boot\drivers\pass.exc', 'rt') as key:
                    key = key.read()
                system('cls')
                mixer('Startup.mp3')
                system('title Dsa Terminal')
                protocol = "MINGW64"
                print(strftime('Starting Dsa Terminal...'))
                print(strftime(f'(C) %Y Dsa Terminal v{__version__} | IP: [{ip}]'))
                print(strftime('===================Dsa Terminal===================')), sleep(0.08)
                timeout = strftime(f'(C) %Y Dsa Terminal v{__version__} | IP: [{ip}] | Computer: [{ftp.host()}]\n')
                if ftp.files.ArquivoExiste('tmp\Booted.log'):
                    ftp.files.Write('tmp\Boted.log', timeout)
                    pass
                elif not ftp.files.ArquivoExiste('tmp\Booted.log'):
                    ftp.files.CriarArquivo('tmp\Boted.log')
                    ftp.files.Write('tmp\Boted.log', timeout)
                while True:
                    try:
                        println(f'┌─────────[\033[32m%username%@{ftp.host()}\033[m] \033[35m{protocol}\033[m \033[34m{pwd}\033[m')
                        cmd: str = input(f'└─$ ').strip()
                        if protocol == 'MSYS':
                            if cmd == 'mingw64':
                                protocol = 'MINGW64'
                                print()
                                continue
                            elif cmd == 'bash':
                                password = getpass('[sudo] Password: ').strip()
                                if key == password:
                                    system('cls')
                                    system('title SUDO: /usr/bin/bash.exe')
                                    system(r'usr\bin\bash.exe')
                                    system('cls')
                                else:
                                    print('[sudo] Password no match!\n')
                                system('title Dsa Terminal')
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
                            elif cmd == 'hostname':
                                system(r'usr\bin\hostname.exe')
                                print('')
                            elif cmd.startswith('nano'):
                                print('Nano is started. . .')
                                system('title [Nano] - Dsa terminal')
                                cmd = cmd.replace('nano ', '')
                                cmd = cmd.replace('nano', '')
                                if cmd == '':
                                    system(rf'usr\bin\nano.exe')
                                    system(f'move {cmd} {win_pwd}')
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
                                    cmd = cmd.replace('%myload%', 'Data not found')
                                if cmd == '/?':
                                    print('Echo: Listagem de parametros\n')
                                    print(r'echo [mensage[format parameters]]')
                                    print(r'\t                Tab')
                                    print(r'\n                To down')
                                    print(r'%myload%          Loaded value')
                                else:
                                    print(cmd)
                                continue
                            elif cmd == 'wmic':
                                print('')
                                system('wmic')
                                continue
                            elif cmd == 'tty':
                                system(r'usr\bin\tty.exe')
                                continue
                            elif 'rm' in cmd:
                                cmd = cmd.replace('rm ', '')
                                cmd = cmd.replace('rm', '')
                                if cmd == '':
                                    print('Remove: Insira um nome-de-arquivo')
                                else:
                                    system(fr'del {win_pwd}\{cmd}')
                                print('')
                            elif cmd.startswith('ls'):
                                cmd = cmd.replace('ls', '')
                                cmd = cmd.replace('ls ', '')
                                system(rf'run\ls.exe {pwd} {cmd}')
                                print('')
                                continue
                            elif cmd == 'ifconfig':
                                print(f'Settings IP and rounts: net[sh-1 gw 192.168.1.1')
                                print(f'IP: [{ip}] Porta: [22]')
                                print(f'Gateway: {route}')
                                print(f'=====================================================')
                                continue
                            elif cmd.startswith('php'):
                                cmd = cmd.replace('php ', '')
                                cmd = cmd.replace('php', '')
                                system(f'var\php\php.exe {cmd}')
                                continue
                            elif cmd == '':
                                print('')
                                continue
                            elif cmd.startswith('psftp'):
                                system('sbin\psftp.exe')
                                print('')
                                continue
                            elif cmd.startswith('touch'):
                                cmd = cmd.replace('touch ', '')
                                cmd = cmd.replace('touch', '')
                                if cmd == '':
                                    open(fr'{pwd}\New file.txt', 'wt+')
                                else:
                                    try:
                                        file = open(fr'{pwd}\{cmd}', 'wt+')
                                    except FileExistsError:
                                        print('Config.: This file alred exist')
                                    else:
                                        print('Config.: Creating file. . .', end=''), sleep(2)
                                        print('finish!!!')
                                        while True:
                                            try:
                                                alinar: str = str(input(''))
                                                ftp.files.Write(fr'{pwd}\{cmd}', alinar)
                                            except:
                                                break
                                    continue
                            elif cmd == 'exit':
                                print('exit'), sleep(2)
                                break
                            elif cmd == 'putty':
                                startfile('sbin\putty.exe')
                                continue
                            elif cmd.startswith('ncat'):
                                cmd = cmd.replace('ncat ', '')
                                cmd = cmd.replace('ncat', '')
                                try:
                                    system(fr'sample\ncat.exe {cmd}')
                                except:
                                    continue
                                continue
                            elif cmd == 'clear':
                                system('cls')
                                continue
                            elif cmd == 'help':
                                print("Help comands of this protocol:")
                                print('Command:             Description:')
                                print('_____________________________________________________')
                                print('cli-http             Console httpie Client')
                                print('hostname             Corrent host name')
                                print('nano [arquivo]       Dsa Terminal E-ditor')
                                print('echo [mensagem]      Write text in console')
                                print('wmic                 All in Windows')
                                print('tty                  Device connected')
                                print('ifconfig             IP and routes this host')
                                print("php                  PHP iNTERPRET")
                                print("psftp                Remote connection")
                                print("touch [arquivo]      Create file")
                                print('putty                Putty driver')
                                print('ncat [parametros]    Netcat')
                                print('clear                Clear console')
                                print('exit                 Exit of Dsa Terminal')
                            else:
                                print(f'shell: {cmd}: command not found!')
                                print('')
                                continue
                        if protocol == 'MINGW64':
                            if cmd == 'msys':
                                protocol = 'MSYS'
                                print('')
                                continue
                            elif cmd.startswith('ftp'):
                                print(bias1, '\n', conn2, '\n', conn1)
                                print(ftp.host(), ' ** ', route, '\n', bias3)
                            elif cmd.startswith('python'):
                                cmd = cmd.replace('python ', '')
                                cmd = cmd.replace('python', '')
                                system(rf'usr\local\Python27\python.exe {win_pwd}\{cmd}')
                            elif cmd.startswith('pip'):
                                cmd = cmd.replace('pip ', '')
                                cmd = cmd.replace('pip', '')
                                system(fr'usr\local\Python27\Scripts\pip.exe {cmd}')
                            elif cmd == 'pkg /?' or cmd == 'pkg':
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
                            elif cmd.startswith('pip3'):
                                cmd = cmd.replace('pip3 ', '')
                                cmd = cmd.replace('pip3', '')
                                system(rf'Python3\Scripts\pip.exe {cmd}')
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
                            elif cmd == 'sudo --version' or cmd == 'sudo -v':
                                print('Dsa Terminal @Root_User v0.0.2020.1')
                                println(rf'root@{host()}')
                            elif cmd == 'hostname':
                                system(r'usr\bin\hostname.exe')
                                print('')
                            elif cmd.startswith('sudo pkg install'):
                                cmd = cmd.replace('sudo ', '')
                                cmd = cmd.replace(' ', '')
                                password = getpass("[sudo] Password: ").strip()
                                if password == key:
                                    ftp.packge.pkg_install(cmd)
                                else:
                                    print('[sudo] Password not found!\n')
                                continue
                            elif cmd.startswith('pkg install'):
                                print('13: Error (Permission DIENED)!')
                                continue
                            elif cmd == 'vlc':
                                system(r'start run\MediaPlayer\vlc.exe')
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
                            elif cmd.startswith('cd'):
                                cmd = cmd.replace('cd ', '')
                                cmd = cmd.replace('cd', '')
                                if cmd == '..':
                                    chdir(fr'{win_pwd}\{cmd}')
                                try:
                                    chdir(fr'{win_pwd}\{cmd}')
                                except:
                                    print('Config.: Dir not found')
                                else:
                                    pwd = fr'{pwd}/{cmd}'
                                    win_pwd = rf'{win_pwd}\{cmd}'
                                print('')
                            elif cmd == 'pwd':
                                print(pwd)
                                continue
                            elif cmd.startswith('pkg uninstall'):
                                print('13: Error (Permission DIENED)!')
                                continue
                            elif cmd.startswith('sudo pkg uninstall'):
                                password = getpass("[sudo] Password: ").strip()
                                if password == key:
                                    ftp.packge.pkg_uninstall(cmd)
                                else:
                                    print('[sudo] Password not found!\n')
                                continue
                            elif cmd.startswith('nano'):
                                print('Nano is started. . .')
                                system('title [Nano] - Dsa terminal')
                                cmd = cmd.replace('nano ', '')
                                cmd = cmd.replace('nano', '')
                                if cmd == '':
                                    system(rf'usr\bin\nano.exe')
                                    system(f'move {cmd} {win_pwd}')
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
                                    cmd = cmd.replace('%myload%', 'Data not found')
                                if cmd == '/?':
                                    print('Echo: Listagem de parametros\n')
                                    print(r'echo [mensage[format parameters]]')
                                    print(r'\t                Tab')
                                    print(r'\n                To down')
                                    print(r'%myload%          Loaded value')
                                else:
                                    print(cmd)
                                continue
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
                            elif cmd == 'changelog':
                                with open('CHANGELOG.TXT') as logme:
                                    print(logme.read())
                            elif cmd == 'arduino':
                                startfile(r'var\Arduino\arduino.exe')
                                continue
                            elif cmd == 'help':
                                print("Help commands of this protocol")
                                print('Command:             Description:')
                                print('_____________________________________________________')
                                print('echo [mensagem]      Write in console')
                                print('pkg [parametros]     Packge manager')
                                print('nano [arquivo]       Dsa Terminal E-ditor')
                                print('ncat [parametros]    NetCat')
                                print('help                 Write help of Dsa Terminal commands')
                                print('tty                  Device connected')
                                print('hostname             Correnct name of host')
                                print('mintty               Mintty Console usr/bin/mintty.exe')
                                print('version              Version and releases of Dsa Terminal')
                                print('ls [parametros]      List all of this dir')
                                print('dir [parametros]     List dir')
                                print('gui                  Phoenix Setup Utility')
                                print("gitlocal             Github.com url of repository")
                                print('./[script or app]    Run. . .')
                                print('firefox              Start firefox')
                                print('issue                Open issue in github')
                                print('cli-http             Console httpie Client')
                                print('pwd                  Path dir')
                                print('mkdir [dir]          Make an dir')
                                print('rm [dirs/files]      Delete diretorys and files')
                                print('touch [file name]    Create file')
                                print('ifconfig             IP and routes this host')
                                print('set [parametros]     Define chars in memorybyte')
                                print('task                 Tasks run in Dsa Terminal')
                                print('exit                 Exit of Dsa Terminal')
                            elif cmd == 'issue':
                                system('mingw64\gh.exe issue create')
                                continue
                            elif cmd.startswith('ncat'):
                                cmd = cmd.replace('ncat ', '')
                                cmd = cmd.replace('ncat', '')
                                try:
                                    system(fr'sample\ncat.exe {cmd}')
                                except:
                                    continue
                                continue
                            elif cmd == 'gitlocal':
                                print('Github: https://github.com/Dsa-Terminal/Dsa-Terminal.git\n')
                                continue
                            elif cmd == 'alone':
                                mixer('Alarm01.wav')
                                print('')
                            elif cmd == '':
                                print('')
                                continue
                            elif cmd == 'prompt':
                                print('')
                                system('pause')
                                continue
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
                                print('exit'), sleep(2)
                                break
                            elif cmd == 'clear':
                                system('cls')
                                continue
                            elif cmd == 'version':
                                print(strftime(f'Dsa Terminal Copyright (C) %Y v{__version__}'))
                                continue
                            elif cmd == 'pkg update':
                                ftp.update()
                                continue
                            elif cmd.startswith('lua'):
                                cmd = cmd.replace('lua ', '')
                                cmd = cmd.replace('lua', '')
                                if cmd == '':
                                    system(r'var\Lua\lua.exe')
                                else:
                                    system(fr'var\Lua\lua.exe {win_pwd}\{cmd}lua')
                                system('title Dsa terminal')
                            elif cmd == 'apimon':
                                system(r'start run\sudo\apimon.exe')
                                print('')
                                continue
                            elif cmd == 'cls':
                                system('cls')
                                continue
                            elif cmd == 'env':
                                system(r'start run\env.exe')
                                print('')
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
                            elif cmd == 'arch':
                                system(r'usr\bin\arch.exe')
                                continue
                            elif cmd == 'id':
                                system(r'usr\bin\id.exe')
                                continue
                            elif cmd == 'mintty':
                                startfile(r'usr\bin\mintty.exe')
                                continue
                            elif cmd == 'date':
                                system(r'usr\bin\date.exe')
                                print('')
                                continue
                            elif cmd == 'gpg':
                                system(r'usr\bin\gpg.exe')
                                continue
                            elif cmd == 'license':
                                with open('LICENSE') as lic:
                                    print(lic.read())
                            elif cmd.startswith('dir'):
                                system(fr'usr\bin\dir.exe {pwd}')
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
                                print('Tasks running in Dsa Terminal:')
                                print('Sevice name:           Local:                   Status:')
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
                                print('Window host            [Serviço do Windows]     Running...')
                                print('Config.                /Terminal.exe            Running...')
                                print('Bash.exe               /bin/bash.exe            Running...')
                                print('Catalogo de Serviço    /server.sc               Running in second instance...')
                                print('Servições do http-cli  /run/http_cli/http.exe   Running in second instance...')
                                print('Github connection      /.git     <dir>          Running...')
                                print('Linux Subsystem        /Terminal.exe            Running in second instance...')
                                print('Gerenciador de Tarefas /Terminal.exe            Running in second instance...')
                                print('mingw64                /mingw64/Main.sh         Running...')
                                print('Phoenix Setup CMOS     /run/SetupUltility/...   Running in second instance...')
                                print('==============================================================================\n')
                            elif cmd == 'tty':
                                system(r'usr\bin\tty.exe')
                                continue
                            elif cmd.startswith('psftp'):
                                system('sbin\psftp.exe')
                                print('')
                                continue
                            elif cmd.startswith('touch'):
                                cmd = cmd.replace('touch ', '')
                                cmd = cmd.replace('touch', '')
                                if cmd == '':
                                    open(fr'{pwd}\New file.txt', 'wt+')
                                else:
                                    try:
                                        file = open(fr'{pwd}\{cmd}', 'wt+')
                                    except FileExistsError:
                                        print('Config.: This file alred exist')
                                    else:
                                        print('Config.: Creating file. . .', end=''), sleep(2)
                                        print('finish!!!')
                                        while True:
                                            try:
                                                alinar: str = str(input(''))
                                                ftp.files.Write(fr'{pwd}\{cmd}', alinar)
                                            except:
                                                break
                                    continue
                            elif cmd == 'gui':
                                ftp.ProgressBar(0.01, "Starting...")
                                system(r'start run\SetupUltility\PhoenixSetupGUI.exe')
                                break
                            elif 'rm' in cmd:
                                cmd = cmd.replace('rm ', '')
                                cmd = cmd.replace('rm', '')
                                if cmd == '':
                                    print('Remove: Insert file a name')
                                else:
                                    system(fr'del {win_pwd}\{cmd}')
                                print('')
                            elif cmd.startswith('ls'):
                                cmd = cmd.replace('ls', '')
                                cmd = cmd.replace('ls ', '')
                                system(rf'run\ls.exe {pwd} {cmd}')
                                print('')
                                continue
                            elif cmd == 'ifconfig':
                                print(f'Settings IP and rounts: net[sh-1 gw 192.168.1.1]')
                                print(f'IP: [{ip}] Porta: [22]')
                                print(f'Gateway: {route}')
                                print(f'=====================================================')
                                continue
                            elif cmd.startswith('php'):
                                cmd = cmd.replace('php ', '')
                                cmd = cmd.replace('php', '')
                                system(f'var\php\php.exe {cmd}')
                                continue
                            elif cmd == 'kernel':
                                try:
                                    startfile('Lib\kernel\main.exe')
                                except FileNotFoundError:
                                    print('Module not instaled in Dsa Terminal')
                                    print('Try:')
                                    print('      sudo pkg install kernel')
                                continue
                            elif cmd == 'ssh':
                                try:
                                    startfile('Lib\ssh\ssh.exe')
                                except FileNotFoundError:
                                    print('Module not instaled in Dsa Terminal')
                                    print('Try:')
                                    print('      sudo pkg install ssh')
                            elif cmd == 'ipxe':
                                i = ftp.iPXE()
                                if i == False:
                                    break
                                else:
                                    continue
                            else:
                                print(f'bash: {cmd}: command not found!')
                                print('')
                                continue
                    except KeyboardInterrupt:
                        i = ftp.iPXE()
                        if i == False:
                            break
                        else:
                            continue
                    except Exception as erro:
                        system('cls')
                        mixer('ERROR_Media.mp3')
                        print('\033[33mFatal:\033[m Dsa Terminal Excepition Interrupt'), sleep(0.111)
                        break
            else:
                system('cls')
                mixer('ERROR_Media.mp3')
                print('Error: No Botable Device')
                print("Don't have a installed System on Dsa Terminal as Device Operative")
                print('PXE MOF: Exiting PXE ROM...'), sleep(6.26)
                auto_get_ProgressBar(0.001)
        else:
            print(f"Config.: Dsa Terminal v{__version__} not was started sucefully")
            print('Config.: Dsa Terminal only started in Windows 10, sorry!')
