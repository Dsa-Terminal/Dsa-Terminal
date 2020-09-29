# Dsa Terminal
![](https://img.shields.io/github/license/Dsa-Terminal/Dsa-Terminal)
![](https://img.shields.io/github/repo-size/Dsa-Terminal/Dsa-Terminal)
![](https://img.shields.io/github/languages/top/Dsa-Terminal/Dsa-Terminal)

The **Dsa Terminal** is a emulator of Gnu/Linux Bash for Windows 10 users!
Totally in portuguese "don't have Englesh version" and with an excellent text formating can do a lot more things than the own Ubuntu!

## Requirements
You do not necessarily need to install Python on your computer, more than you want to install and run `Setup.bat` the first time you use it afterwards, just click on` Terminal.py` and it will run!

If you are an experienced programmer, Python needs two modules for `Terminal.py` to run:

- `python -m pip install rich, tqdm`

If you don't want to install Python 3 https://python.org/downloads you just need to run `Terminal.exe` which will have the same result!

## How to use
Clone this repository using git using the command `git clone https://github.com/Dsa-Terminal/Dsa-Terminal.git master` and then open Cmd.exe and disable
legacy console, open Terminal.exe and type ** help ** you will see all the commands!

# Commands
- `echo ([message])`        Write messages on the screen
- `pkg [parameters]`        Package manager
- `nano [file]`             Dsa Terminal E-ditor
- `ping [parameters]`       Remote network options
- `help`                    Displays help
- `./ Rendashell script]`   Run shell script
- `block`                   Screen saver
- `exit`                    Leaves Dsa Terminal
- `st [Task]`               Starts a Windows task
- `mkdir [folder]`          Create a folder
- `rm`                      Remove ...
- `touch [file]`            Create a file
- `ipconfig`                Shows the computer's IP
- `ls [parameters]`         List of directories and objects
- `node`                    Run node.js serverdev for Dsa Terminal
- `lua`                     Language Lua for Dsa Terminal
- `localhost`               Dsa Terminal Web Page at localhost
_____________________________________________________________________________
To know the parameters of the command type `[command] /?`

# Importing modules
Importing modules into Dsa Terminal is simple; you have to install the module with the command:
- `pkg install [module name]`

And then use the command:
- `Include [module]`

That it will run the `Main.exe` module, to learn more read the documentation at:
`/ run / Docs / Modulos.txt`

# Updates
In the proper ** Dsa Terminal ** type `pkg update` it will fetch the updates and
install them we don't know if you can lose your data in / files / more it will be updated
for the latest version!
## How to know if my Dsa Terminal has been updated
Easy type `version` it will show the current version which will be different from the previous one or
may be the same, but you will see some bugs and new commands in `help`!
Or don't even type it at startup it shows the version!

# News and releases
The core of Dsa Terminal works with Ubuntu and Linux bash, it's like a redistribution
of Linux only that is not exactly like him, for example he does not have the directories:
`/ boot` and` / root` as he does not need a boot and he is already at (root user)!

** See our launches on the launch page **

# How the Dsa Terminal Nucleus works
His Core is in Python 3 plus, he inherits bash from GNU / Linux Ubuntu and GNU / Git
which are essential for the operation and interpretation of shell scripts!

## File structure
The "File structure" has some problems for example the execution of .lua scripts
that he doesn't find in the base in `/ var / Lua` anymore if Dsa Terminal were to move and then delete
would give error, already tried! 1

- *** Wanted contributors ***
### Contributors wanted !!!
The saying goes: * More minds are better *! A good project needs
of contributors for a good performance !!!