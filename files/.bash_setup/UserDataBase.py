from os import system
with open('IPCONFIG.exc', 'wt') as ipconfig:
    ipconfig = ipconfig.read()
class UserDateBase:
    __globals__ = {}
    __annotations__ = {}
    __name__ = {}
    def __init__(self):
        if self.startswith(UserDateBase.__globals__):
            key = 'root@localhost://8000/_index.html'
        for replacemint in key:
            if replacemint == True and self == {}:
                replacemint = replacemint.replace(True, 'Acesso permitido!')
            else:
                replacemint = replacemint.replace(False or None, '13: Acesso negado!')
            return replacemint
        return replacemint
    def __unicode__(self):
        acess = UserDateBase.__init__(self=ipconfig)
        if acess == 'Acesso permitido!':
            acess = '0110101010010101010 @localhost://8000'
        else:
            return acess
        return acess
print(UserDateBase.__unicode__())
system('pause')