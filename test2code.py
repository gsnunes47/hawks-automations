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
        
        #dpk pesquisa
        alttab()
        pg.hotkey('ctrl', '4')
        pg.doubleClick(x=642, y=251)
        pg.hotkey('ctrl', 'a')
        digitar(codigo)
        pg.press('enter')
        time.sleep(1)
        try:
            resultado = pg.locateOnScreen(r'imagens/indisponivel_kdapeca.png')
        except pg.ImageNotFoundException:
            pg.click(x=110, y=537)
            try:
                disponibilidade = pg.locateOnScreen(r'imagens/indisponivel_compel2.png')
            except pg.ImageNotFoundException:
                pg.doubleClick(x=1014, y=260)
                pg.hotkey('ctrl', 'c')
                unformat()
                pg.click(x=1316, y=168)
            else:
                pyperclip.copy('Indisponível')
        else:
            pyperclip.copy('Indisponível')

        if str(pyperclip.paste()) == codigo:
            pyperclip.copy('Indisponível')

        #excel dpk
        alttab()
        pg.click(x=56, y=181)
        pg.write('f' + str(celula_excel))
        pg.press('enter')
        if str(pyperclip.paste()) == 'Indisponível':
            pg.hotkey('ctrl', 'v')
        else:
            pg.write('=')
            pg.hotkey('ctrl', 'v')
            pg.write('+10')
            pg.press('enter')
