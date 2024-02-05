from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['w']]  
codigo = str(produtos[0][0])


# alttab()
# # clickar_imagem_baixo(r'imagens/preco_dpk.png')
# pg.doubleClick(x=1033, y=261)
# pg.click(x=1033, y=261)
# pg.hotkey('ctrl', 'c')
# pyperclip.copy(pyperclip.paste()[2:])
# print(pyperclip.paste()[2:].strip())
# print(pyperclip.paste()[2:].strip())

alttab()
for c in range(0,2):
    pg.click(x=314, y=326)