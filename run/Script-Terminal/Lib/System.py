from os import system
from time import sleep
from random import choice

def init():
	return True
def run(self):
	if self == 'exec as packge':
		return True
	else:
		return False
def cmd(windows_Cmd):
	system(windows_Cmd)
	return True
def echo(msg):
	print(msg)
	return True
def argv(list_options):
	return choice(list_options)
def close():
	exit()
def wait(seconds):
	try:
		a = int(seconds)
	except:
		raise TypeError(f'Traceback (TypeError - {seconds})')
	else:
		sleep(a)
	return True
def sync(value):
	a = (value + 1)
	b = (value + a + 2)
	return value
def suspendConsole():
	system('pause')
	return True
def personalized(msg):
	return msg
def prompt(msg):
	a = input(msg)
	return a
def terminal():
	system(r'start chdir\Terminal.exe')
	close()
def efectued():
	return True
