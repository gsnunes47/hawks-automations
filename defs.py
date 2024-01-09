import pyautogui as pg
import time
import pyperclip

def enquantonao(imagem):
    while True:
        try:
            img = pg.locateOnScreen(imagem)
        except pg.ImageNotFoundException:
            continue
        else:
            print('achei e brequei')
            break
        break
    print()

def clickar_imagem(img):
    x, y, largura, altura = pg.locateOnScreen(img, grayscale=True)
    x = x + largura / 2
    y = y + altura / 2
    pg.click(x, y)

def preencher_campo(info):
    pyperclip.copy(info)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'v')
    pg.press('tab')

def digitar(txt):
    pyperclip.copy(txt)
    pg.hotkey('ctrl', 'v')

def escrever_celula(cell, txt):
    pg.click(x=56, y=181)
    pg.write(cell)
    pg.press('enter')
    time.sleep(0.5)
    pg.write(txt)
    pg.press('enter')
    time.sleep(0.25)

def abrir_site(link): 
    pg.click(x=182, y=67)
    pg.click(x=182, y=67)
    pyperclip.copy(link)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    time.sleep(3)

def unformat():
    pg.press('win')
    time.sleep(0.35)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.35)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.35)
    pg.hotkey('ctrl', 'c')
    time.sleep(0.35)
    pg.press('win')
    pg.press('win')

def alttab():
    pg.hotkey('alt', 'tab')
    time.sleep(0.12)
