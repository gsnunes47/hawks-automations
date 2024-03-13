from defs import *
import pyautogui as pg
import pyperclip
import time

text = 'KIT DE REPARO DO AMORTECEDOR DIANTEIRO DIREITO / ESQUERDO SAMPEL '
text = text.split(' ')
new_text = ''
for c in range(0, 2):
    text.pop()
for i in text:
    new_text += i
    new_text += ' '
text = new_text
print(text)