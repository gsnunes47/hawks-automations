from defs import *
import pyautogui as pg
import pyperclip
import time

pg.FAILSAFE = True

#menu
c = 1 
c2 = 1
produtos = []
while True:
    peça = []
    c2 = 1
    while c2 < 4:
        codigo = pg.password(F'Digite o {c2}º código da {c}ª peça', mask='', title='Cotação RPA')
        if codigo == None:
            break
        peça.append(codigo)
        c2 += 1
    produtos.append(peça)
    c += 1
    escolha = pg.confirm('Deseja continuar?', buttons=['Sim', 'Não'], title='Cotação RPA')
    if escolha == 'Sim':
        continue
    else:
        break

print(produtos)