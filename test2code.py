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

produtos = [['w712/19', 'sp271', 'wo146'], ['lx908', 'c2583', 'fap2831']]
produtos[0].pop(0)

for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()

peca_ai_celula = 3
for peça in produtos:   
    for codigo in peça:

        #pesquisa kdapeca
        alttab()
        pg.hotkey('ctrl', '4')
        pg.doubleClick(x=642, y=251)
        pg.hotkey('ctrl', 'a')
        
        digitar(codigo)
        pg.press('enter')
        time.sleep(2)
        try:
            quantidade = pg.locateOnScreen(r'imagens/enquantonao_kdapeca.png')
        except pg.ImageNotFoundException:
            pyperclip.copy('Indisponível')
        else:
            pg.doubleClick(x=669, y=504)
            pg.hotkey('ctrl', 'c')
            unformat()  

        #excel dpk
        alttab()
        pg.click(x=56, y=181)
        pg.write('f' + str(peca_ai_celula))
        pg.press('enter')
        if str(pyperclip.paste()) == 'Indisponível':
            pg.hotkey('ctrl', 'v')
        else:
            pg.write('=')
            pg.hotkey('ctrl', 'v')
            pg.write('+10')
            pg.press('enter')

        peca_ai_celula += 1
