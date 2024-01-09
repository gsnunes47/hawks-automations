from defs import *
import pyautogui as pg
import time

pg.hotkey('ctrl', 'shift', 'alt', 'win', 'x')
time.sleep(5)
pg.press('tab')
pg.press('tab')
digitar('Planilha de Base para Cotacao')
time.sleep(0.25)
pg.press('enter')
