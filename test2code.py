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

produtos = [['w712/19', 'ph28938928966', 'wo146'], ['lx908', 'c2583', 'fap2831']]
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

        #compel pesquisa
        alttab()
        pg.hotkey('ctrl', '3')
        pg.doubleClick(x=600, y=367)
        pg.hotkey('ctrl', 'a')
        digitar(codigo)
        pg.press('enter')
        time.sleep(2)
        try:
            indisponivel = pg.locateOnScreen(r'imagens/indisponivel_compel.png')
        except pg.ImageNotFoundException:
            try:
                estoque = pg.locateOnScreen(r'imagens/sem_estoque_compel.png')
            except pg.ImageNotFoundException:
                # enquantonao(r'imagens/enquantonao_compel.png') #time.sleep(12)
                pg.doubleClick(x=321, y=630)
                pg.hotkey('ctrl', 'c')
                unformat()
            else:
                pyperclip.copy('Indisponível')
        else:
            pyperclip.copy('Indisponível')
        
        #excel compel
        alttab()
        pg.click(x=56, y=181)
        pg.write('e' + str(peca_ai_celula))
        pg.press('enter')
        if str(pyperclip.paste()) == 'Indisponível':
            pg.hotkey('ctrl', 'v')
        else:
            pg.write('=')
            pg.hotkey('ctrl', 'v')
            pg.write('+10')
            pg.press('enter')
        
        peca_ai_celula += 1
