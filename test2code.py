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
        with pg.hold('ctrl'):
            pg.press('1')
        time.sleep(0.25)
        pg.click(x=204, y=131)
        pesquisa_peca_ai(codigo)
        alttab()
        excel_peca_ai(celula_excel, codigo=codigo)
        
        alttab()
        with pg.hold('ctrl'):
            pg.press('2')
        time.sleep(0.25)
        pg.hotkey('alt', 'left')
        pesquisa_mecanizou(codigo)
        alttab()
        excel_mecanizou(celula_excel)

        alttab()
        with pg.hold('ctrl'):
            pg.press('3')
        time.sleep(0.25)
        pg.hotkey('alt', 'left')
        pesquisa_compel(codigo)
        alttab()
        excel_compel(celula_excel)

        alttab()
        with pg.hold('ctrl'):
            pg.press('4')
        pg.click(x=15, y=518)
        for c in range(0,3):
            pg.press('up')
        pesquisa_kdapeca(codigo)
        alttab()
        excel_kdapeca(celula_excel)