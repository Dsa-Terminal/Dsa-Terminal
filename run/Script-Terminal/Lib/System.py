from os import system
from time import sleep
from random import choice

def init():
	return True
def run(self):
	if self == 'run as packge':
		return True
	else:
		return False
def cmd(windows_Cmd):
	system(windows_Cmd)
	return True
class out:
	def __init__(self):
		return True
	def println(mensagem):
		print(mensagen, end='\n')
		return True
	def print(mensagem):
		print(mensagem, end='')
		return True
def argv(list_options):
	return choice(list_options)
def Close():
	exit()
def wait(seconds):
	try:
		a = int(seconds)
	except:
		raise TypeError(f'Traceback (Error in convert {seconds} in Type >Number<)')
	else:
		sleep(a)
	return True
def sync(value):
	a = (value + 1)
	b = (value + a + 2)
	c = (value + b + 3)
	return c
def suspendConsole():
	system('pause')
	return True
def personalized(msg):
	return msg
def prompt(msg):
	a = input(msg)
	return a
def efectued():
	return True
