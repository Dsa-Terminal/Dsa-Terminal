# Importando modulos
from time import sleep, strftime
from os import mkdir, system
import sys
# Versão do Interpretador
__version__ = '0.0.5'
# Modulos base
import Lib as base
import Lib.System as dll
# Comandos do Sistema
class scripts:
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
		if filename.endswith('.sc'):
			with open(filename, 'rt') as script:
				script = str(script.read())
				if script.startswith('<script ctrl>') and script.endswith('<\script ctrl>'):
					yield script
		else:
			return 'ERROR: O Interpretador so interpreta scripts .sc!'
result = Interpretador.__init__('', "Script.sc")
print(result)