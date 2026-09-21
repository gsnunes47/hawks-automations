from defs import *
import pyautogui as pg
import pyperclip
import time

alttab()

#verificação de login fornecedor_e
contador = 0
while True:
    try:
        if contador == 2:
            pg.moveTo(x=1355, y=135)
            time.sleep(0.5)
            pg.click(x=1244, y=524)
            time.sleep(3.5)
            break
        time.sleep(1)
        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\logado_rmp.png', grayscale=True, confidence=0.9)
    except pg.ImageNotFoundException:
        contador += 1
        continue
    else:
        break
