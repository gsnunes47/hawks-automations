from defs import *
import pyautogui as pg
import pyperclip

# enquantonao()
# preencher_campo()
# clickar_imagem()

# codigo = str(input('Por favor digite o código da peça: '))
codigo = 'sp271'

#abrir o chrome
pg.press('win')
digitar('chrome')
pg.press('enter')
enquantonao(r'imagens/usuario_chrome.png')
clickar_imagem(r'imagens/usuario_chrome.png')

