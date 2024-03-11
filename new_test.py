from defs import *
import pyautogui as pg
import pyperclip
import time

alttab()
pg.doubleClick(x=56, y=181)
pg.write('$C$2:$G$2')
pg.press('enter')
pg.hotkey('ctrl', 'c')

teste = pyperclip.paste()

num = ''
num_list = []
final_list = []
for c in teste:
    if c == ',':
        num += '.'
    elif c == '\t' or c == '\n':
        if c == teste[0]:
            continue
        else:
            num_list.append(num)
            num = ''
    elif c == '\r':
        continue
    else:
        num += c

for i, v in enumerate(num_list):
    if v != 'Indisponível':
        final_list.append(float(v))

try:
    celula = f'{(sum(final_list) / len(final_list)) * 1.8:.2f}'
except ZeroDivisionError:
    pass
else:
    pg.doubleClick(x=56, y=181)
    pg.write('h2')
    pg.press('enter')
    pyperclip.copy(celula)
    pg.hotkey('ctrl', 'v')
pg.press('esc')
