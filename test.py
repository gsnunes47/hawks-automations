from defs import *
import pyautogui as pg
import time

imagem = 'imagens/procurar_peca.ai.png'
codigo = 'sp271'

alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://peca.compel.com.br/')
time.sleep(4)
try:
    img = pg.locateOnScreen(r'imagens/acessar_compel.png')
except pg.ImageNotFoundException:
    pass
else:
    pg.click(x=1248, y=366)
time.sleep(4)
pg.click(x=404, y=417)
digitar(codigo)
pg.press('enter')
time.sleep(8)
pg.click(x=321, y=630)
pg.click(x=321, y=630)
pg.hotkey('ctrl', 'c')
unformat()

#volta pro excel (celula e2)

pg.hold('alt')
pg.press('tab')
pg.press('tab')
pg.click(x=56, y=181)
pg.write('e2')
pg.press('enter')
pg.write('=')
pg.hotkey('ctrl', 'v')
pg.write('+10')
pg.press('enter')