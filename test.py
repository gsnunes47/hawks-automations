from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['94823', 'sp271'], ['wo146'], ['sk421', 'ph2966']]  
codigo = str(produtos[0][0])

#TAB SET
for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()

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
time.sleep(1)
try:
    resultado = pg.locateOnScreen(r'imagens/indisponivel_kdapeca.png')
except pg.ImageNotFoundException:
    pg.click(x=110, y=537)
    try:
        disponibilidade = pg.locateOnScreen(r'imagens/indisponivel_compel2.png')
    except pg.ImageNotFoundException:
        pg.doubleClick(x=1014, y=260)
        pg.hotkey('ctrl', 'c')
        unformat()
        pg.click(x=1316, y=168)
    else:
        pyperclip.copy('Indisponível')
else:
    pyperclip.copy('Indisponível')

if str(pyperclip.paste()) == codigo:
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
