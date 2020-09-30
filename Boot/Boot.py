from os import system

with open('Boot.ini') as opt:
    opt = opt.read()

    if opt.startswith('{'):
        opt = opt.readlines()
opt.run()