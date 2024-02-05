from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

codigo = 'sp271'

alttab()
abrir_site('peca.ai')

#pesquisa peca.ai
time.sleep(3.5) # enquantonao(r'imagens/enquantonao_peca.ai.png')
clickar_imagem(r'imagens/busca_peca.ai.png')
pg.press('tab')
digitar(codigo)

try:
    login = pg.locateOnScreen(r'imagens/logado_peca.ai.png')
except pg.ImageNotFoundException:
    pg.press('enter')
    time.sleep(1)
    # enquantonao(r'imagens/entrar_peca.ai.png')
    for c in range (0, 3):
        pg.press('tab')
    pg.press('enter')
else:
    pg.press('enter')
time.sleep(1.5)

while True:
    try:
        sem_resultado = pg.locateOnScreen(r'imagens/sem_resultado_peca.ai.png')
    except pg.ImageNotFoundException:
        break
    else:
        pg.press('f5')
        time.sleep(1.5)

try:
    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
except pg.ImageNotFoundException:
    # enquantonao(r'imagens/marcas_peca.ai.png')
    # pg.click(x=560, y=690)
    pg.alert('Escolha a peça e depois clique em OK')
    enquantonao(r'imagens/comprar_peca.ai.png')
    pg.click(x=151, y=651)
    pg.click(x=151, y=651)
    pg.hotkey('ctrl', 'c') 
    unformat()
else:
    pyperclip.copy('Indisponível')
