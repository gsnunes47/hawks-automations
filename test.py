from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

codigo = 'sk421'

#pesquisa rmp
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://loja.rmp.com.br/')
pg.click(x=285, y=138)
pg.write(codigo)
pg.press('enter')

enquantonao(r'imagens/enquantonao_rmp2.png')
try:
    sem_resultado = pg.locateOnScreen(r'imagens/sem_resultado_rmp.png')
except pg.ImageNotFoundException:
    try:
        disponibilidade = pg.locateOnScreen(r'imagens/disponivel_rmp.png')
    except:
        pyperclip.copy('Indisponível')
    else:
        enquantonao(r'imagens/enquantonao_rmp.png')
        pg.doubleClick(x=1145, y=562)
        pg.hotkey('ctrl', 'c')
        unformat()
else:
    pyperclip.copy('Indisponível')
    
print(pyperclip.paste())
