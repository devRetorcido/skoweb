
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
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import time
from fake_useragent import UserAgent

ua = UserAgent()
#Actualiza otro navegador
#ua.update()

headers = {"User-Agent": ua.random}


try:

    Website ="https://bo.skokka.com/escorts/santa-cruz/"
    resultado = requests.get(Website,headers=headers)
    resultado.raise_for_status()
    #print(resultado.text)

except HTTPError as http_err:
    print('Errpr HTTP: {}'.format(http_err))
except Exception as err:
    print('Error  {}'.format(err))

#cabecera = resultado.headers["content-type"]
content = resultado.text
#print (content)
soup = BeautifulSoup(content,"html.parser")

#texto_h2 = soup.find('h2')
#print(texto_h2.text)



#h2_todos = soup.find_all("h2",class_="listing-title item-title")
div_todos = soup.find_all('div',class_="item-image-supertop")

#><img src="https://bo-static.imgskk.com/post/7b/f2/7bf26c66390e4deb9160045e36834585.jpg?listing=supertop&amp;v=84ssm3xe" alt="HERMOSA MUJER 😍 DISPONIBLE A CLIENTES EXIGENTES!" class="avatar"></div>)
print (div_todos)
for div in  div_todos:
    imagen = soup.find('v-lazy-image alt')
    print(imagen.text)

    
#print(content)


