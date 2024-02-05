from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['w']]  
codigo = str(produtos[0][0])

# alttab()
# for c in range(0,2):
#     pg.click(x=314, y=326)

alttab()
pg.press('f5')
time.sleep(1.2)
for c in range(0, 16):
    pg.press('tab')