from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

codigo = 'sp271'

#pesquisa rmp
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://loja.rmp.com.br/')
pg.click(x=322, y=125)
pg.write(codigo)
pg.press('enter')
