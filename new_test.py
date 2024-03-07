from defs import *
import pyautogui as pg
import pyperclip
import time

alttab()
clickar_imagem(r'imagens/sifrao_mecanizou.png', 3)
pg.hotkey('ctrl', 'c')
pyperclip.copy(pyperclip.paste()[3:])
# pyperclip.copy