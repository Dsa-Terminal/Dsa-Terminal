from time import sleep, strftime
from os import mkdir, system
import Lib as base
import Lib.System as dll

class scripts;
	def __init__(self):
		return True
	def new(object_new):
		a = object_new
		return a
	def import_api(module):
		if module == 'System':
			return 'System'
		else:
			return module
class Interpretador:
	def __init__(self, filename):
		with open(filename, 'rt') as script:
			script = script.read()
			return script
print('Tudo Certo!')
