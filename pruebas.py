import re
from  bs4  import BeautifulSoup

contenido = """ <html lang="es">
    <head>
    <meta charset="UTF-8">
        <title>Página de prueba</title>
    </head>
    <body>
   <div class="item-image-supertop">
        <v-lazy-image alt="BLANQUITA PIEL FINA RUBIA, EXTRANJERA 😍🤤🤤🤤" 
            class="avatar" src="https://bo-static.imgskk.com/post/35/7a/357ad5ef4d074cf0a9cf4c2f1d7325e9.jpg?listing=supertop&amp;v=84ssm3xe" 
            src-placeholder="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">
    </div>,
    </v-lazy-image>
        <div class="item-image-supertop"><v-lazy-image alt="NEGRITA PIEL FINA RUBIA, EXTRANJERA 😍🤤🤤🤤" class="avatar" src="https://bo-static.imgskk.com/post/26/a0/26a0b276b33d40cb83d73c06553fb925.jpg?listing=supertop&amp;v=84ssm3xe" src-placeholder="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></v-lazy-image></div>'
    </div>
    </body>
</html>
"""

soup = BeautifulSoup(contenido,"html.parser")

titulo = soup.title
lazy = soup.div


print (lazy)