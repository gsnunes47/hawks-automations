from defs import *
import pyautogui as pg
import pyperclip
import time

def zoom():
    pg.hotkey('alt', 'tab')
    with pg.hold('ctrl'):
        time.sleep(0.5)
        pg.scroll(100)
        time.sleep(0.5)
        pg.scroll(100)
        time.sleep(0.5)
        pg.scroll(100)
