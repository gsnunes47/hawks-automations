from defs import *
import pyautogui as pg
import time

imagem = 'imagens/procurar_peca.ai.png'
codigo = 'sp271'

#abrir o chrome
pg.hotkey('win', 'r')
time.sleep(0.25)
digitar('chrome')
pg.press('enter')
time.sleep(1)
pg.hotkey('win', 'up')
abrir_site('peca.ai')

#processo de pesquisa dentro do peca.ai
clickar_imagem(r'imagens/busca_peca.ai.png')
pg.press('tab')
digitar(codigo)
time.sleep(0.25)
pg.press('enter')
time.sleep(1.5)

try:
    img = pg.locateOnScreen(r'imagens/entrar_peca.ai.png')
except pg.ImageNotFoundException:
    pass
else:
    clickar_imagem(r'imagens/entrar_peca.ai.png')

time.sleep(0.5)
pg.press('f5')
time.sleep(3)
pg.click(x=560, y=690)
pg.press('enter')
time.sleep(2)
pg.click(x=151, y=651)
pg.click(x=151, y=651)
pg.hotkey('ctrl', 'c')
unformat()
