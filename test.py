from defs import *
import pyautogui as pg
import pyperclip
import time

c = 1 
c2 = 1
produtos = []
while True:
    peça = []
    c2 = 1
    while c2 < 4:
        codigo = str(input(f"Digite o {c2}º código da {c}ª peça [digite 'parar' para parar]:  "))
        if codigo == 'parar':
            break
        peça.append(codigo)
        c2 += 1
    produtos.append(peça)
    c += 1
    escolha = input('Deseja continuar? [s/n]: ')
    if escolha == 's':
        continue
    else:
        break

produtos[0].pop(0)
print(produtos)
print(produtos[0][0])
print(produtos[0])
