# Importando modulos
from os import system
from time import sleep, strftime
from random import randint, choice
from tqdm import tqdm, trange
from rich.progress import track
# barras de progresso
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
# Installer
auto_get_ProgressBar(0.01)
ProgressBar('Install')
def __init__():
    return True
if __name__ == '__main__':
    __init__()