import socket

hostname = socket.gethostname()
ip = socket.getbyhostname(hostname)

path_started = '/home'
bios = '/run/SetupUltility/PhoenixSetupGUI.exe'
json_starred_config = '/settings.json'

class Bottable:
    