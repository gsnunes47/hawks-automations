from defs import *
import pyautogui as pg
import pyperclip
import time

for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()

def pegar_nome_rmp(tem_nome, celula):
    if tem_nome == True:
        return True
    else:
        alttab()
        pg.doubleClick(x=475, y=260)
        pg.click(x=475, y=260)
        pg.hotkey('ctrl', 'c')
        text = pyperclip.paste()
        text = text.split('-')[0]
        pyperclip.copy(text)
        alttab()
        colar_celula(celula, text)
        return True

pegar_nome_rmp(False, 'a2')