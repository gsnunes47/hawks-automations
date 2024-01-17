from defs import *
import pyautogui as pg
import pyperclip
import time


# text = 'AMORTECEDOR DE SUSPENSÃO TRASEIRO DIREITO / ESQUERDO MONROE - SP271'
# test = text.split('/')[0]
alttab()
pg.doubleClick(x=306, y=316)
pg.click(x=306, y=316)
pg.hotkey('ctrl', 'c')
text = pyperclip.paste().split('/')[0]
print(text)
