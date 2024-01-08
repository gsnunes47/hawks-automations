import pyautogui as pg
import time
import pyperclip

def enquantonao(imagem):
    imagem_na_tela = pg.locateOnScreen(imagem, grayscale=True)
    while not imagem_na_tela:
        imagem_na_tela = pg.locateOnScreen(imagem, grayscale=True)
        time.sleep(0.1)

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
