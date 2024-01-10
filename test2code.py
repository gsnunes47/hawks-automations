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
# codigo = str(produtos[0][0])
produtos = [['sp271', 'sp285']]
produtos[0].pop(0)

for c in range(0,2):
    with pg.hold('alt'):
        pg.press('tab')
        pg.press('tab')
pg.hotkey('alt', 'tab')

for peça in produtos:
    for codigo in peça:
        alttab()
        pg.hotkey('ctrl', '1')
        pg.hotkey('alt', 'left')
        for c in range(0, 8):
            pg.press('tab')
        digitar(codigo)
        pg.press('enter')
        time.sleep(1)
        pg.press('f5')
        try:
            indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
        except pg.ImageNotFoundException:
            # enquantonao(r'imagens/marcas_peca.ai.png')
            pg.click(x=560, y=690)
            enquantonao(r'imagens/comprar_peca.ai.png')
            pg.click(x=151, y=651)
            pg.click(x=151, y=651)
            pg.hotkey('ctrl', 'c') 
            unformat()
        else:
            pyperclip.copy('Indisponível')