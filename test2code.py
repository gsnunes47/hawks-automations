from defs import *
import pyautogui as pg
import pyperclip
import time

# c = 1 
# c2 = 1
# produtos = []
# while True:
#     peça = []
#     c2 = 1
#     while c2 < 4:
#         codigo = str(input(f'Digite o {c2}º código da {c}ª peça: '))
#         peça.append(codigo)
#         c2 += 1
#     produtos.append(peça)
#     c += 1
#     escolha = input('Desaja continuar? [s/n]: ')
#     if escolha == 's':
#         continue
#     else:
#         break

produtos = [['ph2966'], ['4893', '0111247', 'mb9009']]
# codigo = produtos[0][0]

#TAB SET
for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()

celula_peca = 2
for peça in produtos:
    for codigo in peça:
        celula_excel = celula_peca
        #CODIGO DA 2 RODADA AQUI
