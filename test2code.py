from defs import *
import pyautogui as pg
import pyperclip
import time

# TESTE DE MODULARIZAÇÃO SEGUNDA RODADA

produtos = [['t3608','sp271', 'wo1'], ['T36083', 'sp271', 'sk421'], ['vkm4790']]

#TAB SET
for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()

celula_peca = 2
for peça in produtos:
    for codigo in peça:
        celula_excel = celula_peca
        
        alttab()