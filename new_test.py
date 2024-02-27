from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['sp271']]
codigo = produtos[0][0]

alttab()
pg.hotkey('ctrl', 't')
abrir_site('app.mecanizou.com')
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_mecanizou2.png')
pg.press('tab')
pg.write(codigo)
pg.click(x=1162, y=403)
while True:
    try:
        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_mecanizou.png')
    except pg.ImageNotFoundException:
        time.sleep(0.5)
        pg.click(x=1162, y=403)
        continue
    else:
        break

try:
    disponivel = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_mecanizou.png')
except pg.ImageNotFoundException:
    pyperclip.copy('Indisponível')
else:
    pg.click(x=487, y=686)
    time.sleep(0.5)
    pg.doubleClick(x=988, y=403)
    pg.hotkey('ctrl', 'c')
    unformat()


# while True:
#     try:
#         block = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\block_mec.png')
#     except pg.ImageNotFoundException:
#         print('Não esta na tela')
#     else:
#         print('Esta na tela')
