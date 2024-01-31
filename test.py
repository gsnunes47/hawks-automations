from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['ph2960', 'sp271'], ['wo146'], ['sk421', 'ph2966']]  
codigo = str(produtos[0][0])

string = pyperclip.paste()
test = string.split('-')[0]
pyperclip.copy(test)
pg.hotkey('ctrl', 'v')
