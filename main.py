import re
#from colorama import Fore
import requests


Website ='https://bo.skokka.com/escorts/santa-cruz/'
resultado = requests.get(Website)
content = resultado.text
print(content)