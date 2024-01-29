from defs import *
import pyautogui as pg
import pyperclip
import time

produtos = [['ph2960', 'sp271'], ['wo146'], ['sk421', 'ph2966']]  
codigo = str(produtos[0][0])

#compel pesquisa
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
pg.click(x=404, y=417) #verificação
digitar(codigo)
pg.press('enter')
time.sleep(2)

#new process

try:
    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_compel.png')
except pg.ImageNotFoundException:
    try:
        pg.click(x=780, y=585)
        estoque = pg.locateOnScreen(r'imagens/disponivel_compel.png')
    except pg.ImageNotFoundException:
        pyperclip.copy('Indisponível')
    else:
        time.sleep(5)
        pg.doubleClick(x=701, y=339)
        pg.hotkey('ctrl', 'c')
        unformat()
else:
    pyperclip.copy('Indisponível')
