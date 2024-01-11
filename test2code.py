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

produtos = [['w712/19', 'ph2966', 'wo146'], ['lx908', 'c2583', 'fap2831']]
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
        alttab()
        pg.hotkey('ctrl', '1')
        pg.hotkey('alt', 'left')
        time.sleep(1)
        for c in range(0, 8):
            pg.press('tab')
        digitar(codigo)
        pg.press('enter')
        time.sleep(1.5)
        pg.press('f5')
        time.sleep(1.5)
        pg.press('f5')
        time.sleep(1.5)
        try:
            print('Verificando indisponibilidade...')
            indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
        except pg.ImageNotFoundException:
            print('Peça disponível')
            # enquantonao(r'imagens/marcas_peca.ai.png')
            pg.click(x=560, y=690)
            enquantonao(r'imagens/comprar_peca.ai.png')
            pg.click(x=109, y=650)
            pg.click(x=109, y=650)
            pg.hotkey('ctrl', 'c') 
            unformat()
        else:
            print('Peça indisponível')
            pyperclip.copy('Indisponível')
        
        #excel peca.ai
        alttab()
        escrever_celula('b' + str(peca_ai_celula), codigo)
        pg.click(x=23, y=184)
        pg.click(x=23, y=184)
        pg.write('c' + str(peca_ai_celula))
        pg.press('enter')
        if str(pyperclip.paste()) == 'Indisponível':
            pg.hotkey('ctrl', 'v')
        else:
            pg.write('=')
            pg.hotkey('ctrl', 'v')
            pg.write('+15')
            pg.press('enter')
        peca_ai_celula += 1
    