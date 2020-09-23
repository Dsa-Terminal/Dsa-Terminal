__version__ = '1.0'
from os import system
from tqdm import tqdm, trange
from rich.progress import track
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
def auto_get_ProgressBar(time):
    for step in track(range(100)):
        do_step(step, time)
print('Bem-vindo ao Dsa Terminal Updates')
print('Vamos atualizar seu Dsa Terminal para uma versão mais atualizada!')
print('Seus pacotes seram deletados e limparemos o cache do /Temp para otimizar a performace')
system('bin\git.exe clone https://github.com/Dsa-Terminal/Dsa-Terminal')
