from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

produtos = [['w']]  
codigo = str(produtos[0][0])

# alttab()
# for c in range(0,2):
#     pg.click(x=314, y=326)

# abrir o excel
# while True:
#     try:
#         locate = pg.locateOnScreen(r'imagens/enquantonao_mecanizou2.png')
#     except pg.ImageNotFoundException:
#         continue
#     else:
#         print('na tela')

produtos = [['123','321','123123']]
produtos[0].pop(2)