from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['ph2960', 'sp271'], ['wo146'], ['sk421', 'ph2966']]  
codigo = str(produtos[0][0])

#dpk pesquisa
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://www.kdapeca.com.br/login')
time.sleep(5)
pg.doubleClick(x=458, y=496)
time.sleep(1)
pg.press('esc')
time.sleep(0.5)
pg.click(x=301, y=251)
digitar(codigo)
pg.press('enter')
time.sleep(2)
try:
    quantidade = pg.locateOnScreen(r'imagens/enquantonao_kdapeca.png')
except pg.ImageNotFoundException:
    pyperclip.copy('Indisponível')
else:
    pg.doubleClick(x=669, y=504)
    pg.hotkey('ctrl', 'c')
    unformat()  
