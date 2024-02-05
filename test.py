from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = ['t3608', '231231232131', 'wo1', 'T36083', 'sp271', 'sk421', 'vkm4790'] #  
codigo = str(produtos[0])  

#TAB SET
for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)

#dpk pesquisa
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://www.kdapeca.com.br/login')
time.sleep(3.5)
pg.doubleClick(x=1166, y=709)
time.sleep(1)
pg.press('esc')
time.sleep(0.5)
pg.click(x=314, y=326)
digitar(codigo)
pg.press('enter')
time.sleep(1.5)

pg.click(x=901, y=329)
for c in range(0,3):
    pg.press('down')

try:
    comercializado = pg.locateOnScreen(r'imagens/nao_comercializado.png')
except pg.ImageNotFoundException:
    try:
        indisponivel = pg.locateOnScreen(r'imagens/indisponivel_kdapeca.png')
    except pg.ImageNotFoundException:
        try:
            estoque = pg.locateOnScreen(r'imagens/sem_estoque_kdapeca.png')
        except pg.ImageNotFoundException:
            pg.doubleClick(x=788, y=705)
            pg.hotkey('ctrl', 'c')
            unformat()
        else:
            pyperclip.copy('Indisponível')    
    else:
        pyperclip.copy('Indisponível')
else:
    pyperclip.copy('Indisponível')

#excel dpk
alttab()
pg.click(x=56, y=181)
pg.write('f2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+10')
    pg.press('enter')
