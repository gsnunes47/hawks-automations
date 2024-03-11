from defs import *
import pyautogui as pg
import pyperclip
import time

alttab()
pg.doubleClick(x=56, y=181)
pg.write('c5')
pg.press('enter')
# with pg.hold('shift'):
pg.keyDown('shift')
time.sleep(5)
pg.press(['right', 'right', 'right', 'right', 'right'])
pg.keyUp('shift')
pg.hotkey('ctrl', 'c')

teste = pyperclip.paste()
print(teste)
# num = ''
# num_list = []
# final_list = []
# for c in teste:
#     if c == ',':
#         num += '.'
#     elif c == '\t' or c == '\n':
#         if c == teste[0]:
#             continue
#         else:
#             num_list.append(num)
#             num = ''
#     elif c == '\r':
#         continue
#     else:
#         num += c

# # print(num_list)

# for i, v in enumerate(num_list):
#     if v != 'Indisponível':
#         final_list.append(float(v))

# celula = f'{(sum(final_list) / len(final_list)) * 1.8:.2f}'
# print(celula)
