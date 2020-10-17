from os import system
from time import sleep

def init():
	return True
def cmd(windows_Cmd):
	system(windows_Cmd)
	return True
def echo(msg):
	print(msg)
	return True
def close():
	exit()
def wait(seconds):
	try:
		a = int(seconds)
	except:
		print(f'Traceback (TypeError - {seconds}) value incorrect!')
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
def prompt(msg):
	a = input(msg)
	return a
def efectued():
	return True