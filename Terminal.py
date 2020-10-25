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
import socket, serial
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
    print('Lendo pacotes de https://github.com/Dsa-Terminal/Dsa-Terminal.git....'), sleep(0.01)
    print('Git 1: https://github.com/Dsa-Terminal/Dsa-Terminal/releases....'), sleep(0.023)
    print('Git 2: https://github.com/Dsa-Terminal/Dsa-Terminal/commit/22af2ee0b1d92e9b3ebe909d5371324e0ee717e2...'), sleep(1)
    print('[Trabalhando em atualizações]...', end=''), sleep(2.934)
    print('Concluido!!')
    print('Git 3: https://github.com/Dsa-Terminal/Dsa-Terminal/releases/ [Processando...]'), sleep(0.02)
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
            print('Pkg: Insira-um-nome-de-pacote-valido\n')
        elif cmd == 'Dsa-Terminal':
            print('Pkg: Para atualizar o Dsa Terminal você deve usar o comando "pkg update"\n')
        else:
            print(f'Lendo coleção https://github.com/Dsa-Terminal/{cmd}...'), sleep(0.01)
            print(f'Git 1: [Downloading...] https://github.com/Dsa-Terminal/{cmd}/releases/download/{cmd}-master.zip'), sleep(1)
            auto_get_ProgressBar(0.001)
            print(f'Git 2: https://github.com/Dsa-Terminal/{cmd}/commit/22af2ee0b1e9b3ebe909d5371324e0ee717e2...'), sleep(1.92)
            print(f'Git 3: [Making Dependences...][Building Setup.exe].....'), sleep(0.002)
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
class CallTree:
    """ This class provides a tree representation of the functions
        call stack. If a function has no parent in the kernel (interrupt,
        syscall, kernel thread...) then it is attached to a virtual parent
        called ROOT.
    """
    ROOT = None
    def __init__(self, func, time=None, parent=None):
        self._func = func
        self._time = time
        if parent is None:
            self._parent = CallTree.ROOT
        else:
            self._parent = parent
        self._children = []
    def calls(self, func, calltime):
        """ If a function calls another one, call this method to insert it
            into the tree at the appropriate place.
            @return: A reference to the newly created child node.
        """
        child = CallTree(func, calltime, self)
        self._children.append(child)
        return child
    def getParent(self, func):
        """ Retrieve the last parent of the current node that
            has the name given by func. If this function is not
            on a parent, then create it as new child of root
            @return: A reference to the parent.
        """
        tree = self
        while tree != CallTree.ROOT and tree._func != func:
            tree = tree._parent
        if tree == CallTree.ROOT:
            child = CallTree.ROOT.calls(func, None)
            return child
        return tree
    def __repr__(self):
        return self.__toString("", True, "")
    def __toString(self, branch, lastChild):
        if self._time is not None:
            s = "%s----%s (%s)\n" % (branch, self._func, self._time)
        else:
            s = "%s----%s\n" % (branch, self._func)

        i = 0
        if lastChild:
            branch = branch[:-1] + " "
        while i < len(self._children):
            if i != len(self._children) - 1:
                s += "%s" % self._children[i].__toString(branch +\
                                "    |", False)
            else:
                s += "%s" % self._children[i].__toString(branch +\
                                "    |", True)
            i += 1
        return s
def CachedType(selfed):
    return selfed[1], True
class gdb:
    def __init__(self):
        super(gdb, self).__init__("GDB")
        return self.__init__(gdb)
    def Value(self):
        RESULT = int(self[1])
        return RESULT
    def execute(self, to_string):
        self.execute("endian", to_string=to_string)
        requests = [f'little endian {to_string}', f'big endian {to_string}', '1028']
        return choice(requests)
    def GdbError(self, msg):
        return msg
    def write(self):
        print(self, end='', sep='')
        return True
target_endianness = None
list_head = CachedType(route)
class DeviceLinuxDriverAssert:
    """Calibrador e depurador do iExecutor do Device de Driver Linux do Dsa Terminal"""
    def __init__(self):
        calibre = super(DeviceLinuxDriverAssert, self)
        return True, calibre
    def offset_of(typeobj, field):
        element = gdb.Value(0)
        return int(str(element[field].address).split()[0], 16)
    def container_of(ptr, typeobj, member):
        return (ptr.cast(get_long_type()) -
                offset_of(typeobj, member)).cast(typeobj)
    def get_long_type():
        long_type = CachedType("long")
        return long_type.get_type()
    def list_for_each(head):
        if head.type == list_head.get_type().pointer():
            head = head.dereference()
        elif head.type != list_head.get_type():
            raise TypeError("Must be struct list_head not {}".format(head.type))
        node = head['next'].dereference()
        while node.address != head.address:
            yield node.address
            node = node['next'].dereference()
    def get_target_endianness(self, LITTLE_ENDIAN, MEDIUM_ENDIAN ,BIG_ENDIAN):
        global target_endianness
        if target_endianness is None:
            endian = gdb.execute("show endian", to_string=True)
            if "little endian" in endian:
                target_endianness = LITTLE_ENDIAN
            elif "medium endian" in endian:
                target_endianness = MEDIUM_ENDIAN
            elif "big endian" in endian:
                target_endianness = BIG_ENDIAN
            else:
                raise gdb.GdbError("unknown endianness '{0}'".format(str(endian)))
        return target_endianness
    def read_u16(buffer, offset, LITTLE_ENDIAN, get_target_endianness):
        buffer_val = buffer[offset:offset + 2]
        value = [0, 0]

        if type(buffer_val[0]) is str:
            value[0] = ord(buffer_val[0])
            value[1] = ord(buffer_val[1])
        else:
            value[0] = buffer_val[0]
            value[1] = buffer_val[1]

        if get_target_endianness == LITTLE_ENDIAN:
            return value[0] + (value[1] << 8)
        else:
            return value[1] + (value[0] << 8)
    def read_u32(buffer, offset, LITTLE_ENDIAN, get_target_endianness):
        if get_target_endianness == LITTLE_ENDIAN:
            return read_u16(buffer, offset) + (read_u16(buffer, offset + 2) << 16)
        else:
            return read_u16(buffer, offset + 2) + (read_u16(buffer, offset) << 16)
    def read_u64(buffer, offset, LITTLE_ENDIAN, get_target_endianness):
        if get_target_endianness == LITTLE_ENDIAN:
            return read_u32(buffer, offset) + (read_u32(buffer, offset + 4) << 32)
        else:
            return read_u32(buffer, offset + 4) + (read_u32(buffer, offset) << 32)
class Arduino:
    __module__ = 'Arduino UNO'
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
            elif 'endian' in cmd:
                target_endianness = DeviceLinuxDriverAssert.get_target_endianness(self="", 
                                                                                LITTLE_ENDIAN='<endian="0">',
                                                                                MEDIUM_ENDIAN='<endian="512">',
                                                                                BIG_ENDIAN='<endian="1024">')
                print(target_endianness)
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
            elif cmd == 'cli-ino':
                print('')
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
                print('endian               Ganha um novo código de endian')
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
            elif cmd == '':
                for d in range(0, 1):
                    continue
                del d
            elif cmd == 'prompt':
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
                continue
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
                    startfile('Lib\kernel\main.exe')
                except FileNotFoundError:
                    print('Modulo não instalado no sistema do Dsa Terminal!')
                    print('Tente:')
                    print('      sudo pkg install kernel')
                continue
            elif cmd == 'ssh':
                try:
                    startfile('Lib\ssh\main.exe')
                except FileNotFoundError:
                    print('Modulo não instalado no sistema do Dsa Terminal!')
                    print('Tente:')
                    print('      sudo pkg install ssh')
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
