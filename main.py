
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

#instalar el webdriver de chrome
#driver = webdriver.Chrome(ChromeDriverManager().install())

#navegar a website
#driver.get ("https://bo.skokka.com/escorts/santa-cruz/")

# cerrar navegador y sesonp
#driver.quit()
#time.sleep(10)


import re
#from colorama import Fore
import requests
import time

Website ="https://bo.skokka.com/escorts/santa-cruz/"


resultado = requests.get(Website)
cabecera = resultado.headers["content-type"]
content = resultado.text
print(cabecera)
print("*",30)
#print(content)


