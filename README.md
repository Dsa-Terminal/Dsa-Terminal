# Dsa Terminal
![](https://img.shields.io/github/license/Dsa-Terminal/Dsa-Terminal)
![](https://img.shields.io/github/repo-size/Dsa-Terminal/Dsa-Terminal)
![](https://img.shields.io/github/languages/top/Dsa-Terminal/Dsa-Terminal)

Read in [English](https://github.com/Dsa-Terminal/Dsa-Terminal/blob/master/ENGLISH_README.md)

O **Dsa Terminal** é um emulador do Bash do Gnu/Linux Ubuntu para usuarios do Windows 10!
Totalmente em português e com uma excelente formatação de texto pode realizar muito mais coisa que o propio Ubuntu.

## Pré-Requisitos
Você não necessariamente precisa instalar o Python no seu computador, mais de quiser pode instalar e executar o `Setup.bat` da primeira vez que usar depois é só clicar em `Terminal.py` que ele sera executado!

Se você é um programador experiente o Python precisa de dois modulos para o `Terminal.py` ser executado:

- `python -m pip install rich, tqdm`

Senão quiser instalar o Python 3 https://python.org/downloads você só precisa executar `Terminal.exe` que tera o mesmo resultado!

## Como Usar
Clone este repositorio usando o git através do comando `git clone https://github.com/Dsa-Terminal/Dsa-Terminal.git master` e depois abra o Cmd.exe e desative o 
console herdado, abra o Terminal.exe e digite **help** que você vera todos os comandos!

# Comandos
- `echo([mensagem])`    Escreve mensagens na tela
- `pkg [parametros]`    Gerenciador de pacotes
- `nano [arquivo]`      Dsa Terminal E-ditor
- `ping [parametros]`   Opções de rede remota
- `help`                Exibe ajuda
- `./[shell script]`    Executa shell script
- `block`               Protetor de tela
- `exit`                Sai do Dsa Terminal
- `st [Tarefa]`         Começa uma tarefa do Windows
- `mkdir [pasta]`       Cria uma pasta
- `rm`                  Remover...
- `touch [arquivo]`     Cria um arquivo
- `ipconfig`            Mostra o IP do computador
- `ls [parametros`      Listagem de diretorios e objetos
- `node`                Executa node.js serverdev for Dsa Terminal
- `lua`                 Linguagem Lua for Dsa Terminal
- `localhost`           Dsa Terminal Web Page no localhost
_____________________________________________________________________________
Para saber os parametros do comando digite `[comando] /?`

# Importando módulos
A importação de modulos no Dsa Terminal é simples; você tem de instalar o modulo com o comando:
- `pkg install [nome do modulo]`

E depois usar o comando:
- `Incluide [modulo]`

Que ele ira executar o `Main.exe` do modulo, para saber mais leia a documentação que está em:
`/run/Docs/Modulos.txt`

# Updates
No propio **Dsa Terminal** digite `pkg update` ele irá buscar aas atualizações e
as instalar não sabemos se você pode perder seus dados em /files/ mais ele sera atualizado
para a ultima versão!
## Como saber se meu Dsa Terminal foi atualizado
Facil digite `version` que ele mostra-ra a versão atual que já sera diferente da anterior ou 
pode ser a mesma, mais você verá alguns bugs e novos comandos em `help`!
Ou nem digite na inicialização ele mostra a versão!

# Novidades e lançamentos
O nucleo do Dsa Terminal funciona com o bash do Ubuntu e Linux, é como uma redistribuição 
do Linux só que não é exatamente igual ele, por exemplo ele não tem os diretorios:
`/boot` e `/root` pois ele não precisa de boot e ele já esta no (root user)! 

**Veja os nosso lançamentos na pagina dos lançamentos**

# Como funciona o Nucleo do Dsa Terminal
O Core dele é em Python 3 mais, ele herda o bash do GNU/Linux Ubuntu e GNU/Git
que são esenciais para o funcionamento e a interpretação de shell script!

## Estrutura de arquivos
A "Estrutura de arquivos" tem alguns poblemas por exemplo a execução de scripts .lua
que ele não encontra na base em `/var/Lua` mais se o Dsa Terminal fosse mover e depois excluir
iria dar erro, já tentei!1

- ***Procura-se contibuidores***
### Procura-se contribuidores!!!
Já diz o ditado: *Mais mentes pensam melhor*! Um projeto bom precisa
de contribuidores para um bom desempenho!!!
