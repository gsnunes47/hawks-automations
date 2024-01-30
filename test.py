from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['ph2960', 'sp271'], ['wo146'], ['sk421', 'ph2966']]  
codigo = str(produtos[0][0])

for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()

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
try:
    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_compel.png')
except pg.ImageNotFoundException:
    try:
        pg.click(x=780, y=585)
        time.sleep(1.5)
        estoque = pg.locateOnScreen(r'imagens/disponivel_compel.png')
    except pg.ImageNotFoundException:
        pg.click(x=1125, y=147)
        pyperclip.copy('Indisponível')
    else:
        while True:
            try:
                preco = pg.locateOnScreen(r'imagens/preco_compel.png')
            except pg.ImageNotFoundException:
                continue
            else:
                break
        pg.doubleClick(x=701, y=339)
        pg.hotkey('ctrl', 'c')
        unformat()
        time.sleep(0.1)
        pg.click(x=1125, y=147)
else:
    pyperclip.copy('Indisponível')


#excel compel
alttab()
pg.click(x=56, y=181)
pg.write('e2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+10')
    pg.press('enter')
