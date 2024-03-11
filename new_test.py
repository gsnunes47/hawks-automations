from defs import *
import pyautogui as pg
import pyperclip
import time

teste = pyperclip.paste()

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
#     else:
#         num += c

# for i, v in enumerate(num_list):
#     if v != 'Indisponível':
#         print(v)
#     #     final_list.append(float(v))

# # celula = f'{(sum(final_list) / len(final_list)) * 1.8:.2f}'
# # print(celula)