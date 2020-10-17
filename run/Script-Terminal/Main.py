from time import sleep, strftime
from os import mkdir, system
import Lib as base
import Lib.System as dll

class Interpretador:
	def __init__(self, filename):
		with open(filename, 'rt') as script:
			script = script.read()
			return script
print('Tudo Certo!')
