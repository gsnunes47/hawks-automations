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

for c in range(0,2):
    with pg.hold('alt'):
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)
    print()


#loop a partir do segundo código    
celula_peca = 2
for peça in produtos:
    celula_excel = celula_peca
    if peça == produtos[0]:
        celula_peca = 3
        celula_excel = celula_peca
        for codigo in peça:
            if codigo == peça[0]:
                celula_peca = 5
                pass
            elif codigo == peça[-1]:
                
                alttab()
                pg.hotkey('ctrl', '1')
                pg.hotkey('alt', 'left')
                time.sleep(1)
                for c in range(0, 8):
                    pg.press('tab')
                digitar(codigo)
                pg.press('enter')
                time.sleep(1.5)
                while True:
                    try:
                        sem_resultado = pg.locateOnScreen(r'imagens/sem_resultado_peca.ai.png')
                    except pg.ImageNotFoundException:
                        break
                    else:
                        pg.press('f5')
                        time.sleep(1.5)
                try:
                    print('Verificando indisponibilidade...')
                    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
                except pg.ImageNotFoundException:
                    print('Peça disponível')
                    enquantonao(r'imagens/marcas_peca.ai.png')
                    pg.click(x=560, y=690)
                    enquantonao(r'imagens/comprar_peca.ai.png')
                    pg.click(x=109, y=650)
                    pg.click(x=109, y=650)
                    pg.hotkey('ctrl', 'c') 
                    unformat()
                else:
                    print('Peça indisponível')
                    pyperclip.copy('Indisponível')
                
                # excel peca.ai
                alttab()
                escrever_celula('b' + str(celula_excel), codigo)
                pg.click(x=23, y=184)
                pg.click(x=23, y=184)
                pg.write('c' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+15')
                    pg.press('enter')

                #pesquisa mecanizou
                alttab()
                pg.hotkey('ctrl', '2')
                pg.hotkey('alt', 'left')
                time.sleep(3)
                pg.press('tab')
                digitar(codigo)         
                pg.press('enter')
                time.sleep(3)
                try:
                    disponivel = pg.locateOnScreen(r'imagens/enquantonao_mecanizou.png')
                except pg.ImageNotFoundException:
                    pyperclip.copy('Indisponível')
                else:
                    pg.click(x=500, y=491)
                    time.sleep(0.5)
                    pg.doubleClick(x=988, y=403)
                    pg.hotkey('ctrl', 'c')
                    unformat()

                #excel mecanizou
                alttab()
                pg.click(x=56, y=181)
                pg.write('d' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+7')
                    pg.press('enter')

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
                pg.write('e' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')

                #pesquisa dpk
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
                pg.write('f' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')

                celula_peca = 5
            else:

                alttab()
                pg.hotkey('ctrl', '1')
                pg.hotkey('alt', 'left')
                time.sleep(1)
                for c in range(0, 8):
                    pg.press('tab')
                digitar(codigo)
                pg.press('enter')
                time.sleep(1.5)
                while True:
                    try:
                        sem_resultado = pg.locateOnScreen(r'imagens/sem_resultado_peca.ai.png')
                    except pg.ImageNotFoundException:
                        break
                    else:
                        pg.press('f5')
                        time.sleep(1.5)
                try:
                    print('Verificando indisponibilidade...')
                    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
                except pg.ImageNotFoundException:
                    print('Peça disponível')
                    enquantonao(r'imagens/marcas_peca.ai.png')
                    pg.click(x=560, y=690)
                    enquantonao(r'imagens/comprar_peca.ai.png')
                    pg.click(x=109, y=650)
                    pg.click(x=109, y=650)
                    pg.hotkey('ctrl', 'c') 
                    unformat()
                else:
                    print('Peça indisponível')
                    pyperclip.copy('Indisponível')
                
                # excel peca.ai
                alttab()
                escrever_celula('b' + str(celula_excel), codigo)
                pg.click(x=23, y=184)
                pg.click(x=23, y=184)
                pg.write('c' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+15')
                    pg.press('enter')

                #pesquisa mecanizou
                alttab()
                pg.hotkey('ctrl', '2')
                pg.hotkey('alt', 'left')
                time.sleep(3)
                pg.press('tab')
                digitar(codigo)         
                pg.press('enter')
                time.sleep(3)
                try:
                    disponivel = pg.locateOnScreen(r'imagens/enquantonao_mecanizou.png')
                except pg.ImageNotFoundException:
                    pyperclip.copy('Indisponível')
                else:
                    pg.click(x=500, y=491)
                    time.sleep(0.5)
                    pg.doubleClick(x=988, y=403)
                    pg.hotkey('ctrl', 'c')
                    unformat()

                #excel mecanizou
                alttab()
                pg.click(x=56, y=181)
                pg.write('d' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+7')
                    pg.press('enter')

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
                pg.write('e' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')

                #pesquisa dpk
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
                pg.write('f' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')
                
                celula_excel += 1
    else:
        for codigo in peça:
            if codigo == peça[0]:
                alttab()
                pg.hotkey('ctrl', '1')
                pg.hotkey('alt', 'left')
                time.sleep(1)
                for c in range(0, 8):
                    pg.press('tab')
                digitar(codigo)
                pg.press('enter')
                time.sleep(1.5)
                while True:
                    try:
                        sem_resultado = pg.locateOnScreen(r'imagens/sem_resultado_peca.ai.png')
                    except pg.ImageNotFoundException:
                        break
                    else:
                        pg.press('f5')
                        time.sleep(1.5)
                try:
                    print('Verificando indisponibilidade...')
                    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
                except pg.ImageNotFoundException:
                    print('Peça disponível')
                    enquantonao(r'imagens/marcas_peca.ai.png')
                    pg.click(x=560, y=690)
                    enquantonao(r'imagens/comprar_peca.ai.png')
                    pg.click(x=109, y=650)
                    pg.click(x=109, y=650)
                    pg.hotkey('ctrl', 'c') 
                    unformat()
                else:
                    print('Peça indisponível')
                    pyperclip.copy('Indisponível')
                
                # excel peca.ai
                alttab()
                escrever_celula('b' + str(celula_excel), codigo)
                pg.click(x=23, y=184)
                pg.click(x=23, y=184)
                pg.write('c' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+15')
                    pg.press('enter')

                #pegar nome da peça
                alttab()
                pg.doubleClick(x=306, y=316)
                pg.click(x=306, y=316)
                pg.hotkey('ctrl', 'c')
                text = pyperclip.paste().split('/')[0]
                alttab()
                escrever_celula('a' + str(celula_excel), text)

                #pesquisa mecanizou
                alttab()
                pg.hotkey('ctrl', '2')
                pg.hotkey('alt', 'left')
                time.sleep(3)
                pg.press('tab')
                digitar(codigo)         
                pg.press('enter')
                time.sleep(3)
                try:
                    disponivel = pg.locateOnScreen(r'imagens/enquantonao_mecanizou.png')
                except pg.ImageNotFoundException:
                    pyperclip.copy('Indisponível')
                else:
                    pg.click(x=500, y=491)
                    time.sleep(0.5)
                    pg.doubleClick(x=988, y=403)
                    pg.hotkey('ctrl', 'c')
                    unformat()

                #excel mecanizou
                alttab()
                pg.click(x=56, y=181)
                pg.write('d' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+7')
                    pg.press('enter')

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
                pg.write('e' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')

                #pesquisa dpk
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
                pg.write('f' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')
            else:
                alttab()
                pg.hotkey('ctrl', '1')
                pg.hotkey('alt', 'left')
                time.sleep(1)
                for c in range(0, 8):
                    pg.press('tab')
                digitar(codigo)
                pg.press('enter')
                time.sleep(1.5)
                while True:
                    try:
                        sem_resultado = pg.locateOnScreen(r'imagens/sem_resultado_peca.ai.png')
                    except pg.ImageNotFoundException:
                        break
                    else:
                        pg.press('f5')
                        time.sleep(1.5)
                try:
                    print('Verificando indisponibilidade...')
                    indisponivel = pg.locateOnScreen(r'imagens/indisponivel_peca.ai.png')
                except pg.ImageNotFoundException:
                    print('Peça disponível')
                    enquantonao(r'imagens/marcas_peca.ai.png')
                    pg.click(x=560, y=690)
                    enquantonao(r'imagens/comprar_peca.ai.png')
                    pg.click(x=109, y=650)
                    pg.click(x=109, y=650)
                    pg.hotkey('ctrl', 'c') 
                    unformat()
                else:
                    print('Peça indisponível')
                    pyperclip.copy('Indisponível')
                
                # excel peca.ai
                alttab()
                escrever_celula('b' + str(celula_excel), codigo)
                pg.click(x=23, y=184)
                pg.click(x=23, y=184)
                pg.write('c' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+15')
                    pg.press('enter')

                #pesquisa mecanizou
                alttab()
                pg.hotkey('ctrl', '2')
                pg.hotkey('alt', 'left')
                time.sleep(3)
                pg.press('tab')
                digitar(codigo)         
                pg.press('enter')
                time.sleep(3)
                try:
                    disponivel = pg.locateOnScreen(r'imagens/enquantonao_mecanizou.png')
                except pg.ImageNotFoundException:
                    pyperclip.copy('Indisponível')
                else:
                    pg.click(x=500, y=491)
                    time.sleep(0.5)
                    pg.doubleClick(x=988, y=403)
                    pg.hotkey('ctrl', 'c')
                    unformat()

                #excel mecanizou
                alttab()
                pg.click(x=56, y=181)
                pg.write('d' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+7')
                    pg.press('enter')

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
                pg.write('e' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')

                #pesquisa dpk
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
                pg.write('f' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+10')
                    pg.press('enter')
            celula_excel += 1
        celula_peca += 3
