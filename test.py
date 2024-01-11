from defs import *
import pyautogui as pg
import pyperclip
import time

# teste = pyperclip.paste()
# print(teste)

produtos = [2,3,3,4,56,6]
for peça in produtos:
    print(f'Peça {produtos.index(peça)} cadastrada.')