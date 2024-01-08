import pyautogui as pg
import time
import pyperclip

def enquantonao(imagem):
    imagem_na_tela = pg.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    while not imagem_na_tela:
        imagem_na_tela = pg.locateOnScreen(imagem, grayscale=True, confidence=0.9)
        time.sleep(0.1)

def clickar_imagem(img):
    x, y, largura, altura = pg.locateOnScreen(img, grayscale=True, confidence=0.9)
    x = x + largura / 2
    y = y + altura / 2
    pg.click(x, y)

def preencher_campo(info):
    pyperclip.copy(info)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'v')
    pg.press('tab')
