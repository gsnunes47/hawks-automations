from defs import *
import pyautogui as pg
import pyperclip
import time

# TESTE DE MODULARIZAÇÃO SEGUNDA RODADA

produtos = [['w719/30','sp271'], ['T36083', 'sp271', 'sk421'], ['vkm4790']]

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
    celula_excel = celula_peca
    if peça == produtos[0]:
        celula_peca = 3
        celula_excel = celula_peca
        for codigo in peça:
            
            # precesso peca.ai
            alttab()
            pg.hotkey('ctrl', '1')
            while True:
                try:
                    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\marcas_peca.ai.png')
                except pg.ImageNotFoundException:
                    pg.hotkey('alt', 'left')
                    while True:
                        try:
                            img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\marcas_peca.ai.png')
                        except pg.ImageNotFoundException:
                            continue
                        else:
                            break
                    break
                else:
                    break
            pg.click(x=0, y=371)
            pg.press('home')
            pg.doubleClick(x=482, y=333)
            pg.hotkey('ctrl', 'a')
            pg.write(codigo)
            pg.press('tab')
            pg.press('enter')
            
            #escolha manual peca ai segunda rodada
            choice = pg.confirm('Escolha a peça e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\comprar_peca.ai.png')
                pg.click(x=151, y=651)
                pg.click(x=151, y=651)
                pg.hotkey('ctrl', 'c') 
                unformat()

            #excel peca.ai
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
            
            #processo mecanizou
            alttab()
            pg.hotkey('ctrl', '2')
            pg.hotkey('alt', 'left')
            enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_mecanizou2.png')
            pg.press('tab')
            pg.write(codigo)
            pg.click(x=1162, y=403)
            while True:
                try:
                    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\marca_mecanizou.png')
                except pg.ImageNotFoundException:
                    time.sleep(1.5)
                    pg.click(x=1162, y=403)
                    continue
                else:
                    break

            choice = pg.confirm('Escolha a peça e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
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

            #processo compel
            alttab()
            pg.hotkey('ctrl', '3')
            pg.click(x=1, y=255)
            pg.press('home')
            time.sleep(1)
            pg.doubleClick(x=600, y=367)
            pg.hotkey('ctrl', 'a')
            digitar(codigo)
            pg.press('enter')
            time.sleep(3.5)

            choice = pg.confirm('Escolha a peça, clique em detalhes e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\preco_compel.png')
                pg.doubleClick(x=701, y=339)
                pg.hotkey('ctrl', 'c')
                unformat()
                time.sleep(0.1)
                pg.click(x=1125, y=147)

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

            #processo dpk
            alttab()
            pg.hotkey('ctrl', '4')
            time.sleep(0.3)
            pg.click(x=1, y=255)
            pg.press('home')
            time.sleep(1)
            pg.doubleClick(x=346, y=319)
            pg.hotkey('ctrl', 'a')
            digitar(codigo)
            pg.press('enter')
            choice = pg.confirm('Escolha a peça, copie o código interno e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
                pg.press('home')
                time.sleep(1)
                pg.doubleClick(x=346, y=319)
                pg.hotkey('ctrl', 'a')
                pg.hotkey('ctrl', 'v')
                pg.press('enter')
                time.sleep(1.5)
                pg.click(x=901, y=329)
                for c in range(0,3):
                    pg.press('down')
                pg.doubleClick(x=788, y=705)
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

            # precesso peca.ai
            alttab()
            pg.hotkey('ctrl', '1')
            while True:
                try:
                    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\marcas_peca.ai.png')
                except pg.ImageNotFoundException:
                    pg.hotkey('alt', 'left')
                    while True:
                        try:
                            img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\marcas_peca.ai.png')
                        except pg.ImageNotFoundException:
                            continue
                        else:
                            break
                    break
                else:
                    break
            pg.doubleClick(x=482, y=333)
            pg.hotkey('ctrl', 'a')
            pg.write(codigo)
            pg.press('tab')
            pg.press('enter')
            
            #escolha manual peca ai segunda rodada
            choice = pg.confirm('Escolha a peça e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\comprar_peca.ai.png')
                pg.click(x=151, y=651)
                pg.click(x=151, y=651)
                pg.hotkey('ctrl', 'c') 
                unformat()

            #excel peca.ai
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
            
            #processo mecanizou
            alttab()
            pg.hotkey('ctrl', '2')
            pg.hotkey('alt', 'left')
            enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_mecanizou2.png')
            pg.press('tab')
            pg.write(codigo)
            pg.click(x=1162, y=403)
            while True:
                try:
                    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\marca_mecanizou.png')
                except pg.ImageNotFoundException:
                    time.sleep(1.5)
                    pg.click(x=1162, y=403)
                    continue
                else:
                    break

            choice = pg.confirm('Escolha a peça e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
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

            #processo compel
            alttab()
            pg.hotkey('ctrl', '3')
            pg.click(x=1, y=255)
            pg.press('home')
            time.sleep(1)
            pg.doubleClick(x=600, y=367)
            pg.hotkey('ctrl', 'a')
            digitar(codigo)
            pg.press('enter')
            time.sleep(3.5)

            choice = pg.confirm('Escolha a peça, clique em detalhes e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\preco_compel.png')
                pg.doubleClick(x=701, y=339)
                pg.hotkey('ctrl', 'c')
                unformat()
                time.sleep(0.1)
                pg.click(x=1125, y=147)

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

            #processo dpk
            alttab()
            pg.hotkey('ctrl', '4')
            time.sleep(0.3)
            pg.click(x=1, y=255)
            pg.press('home')
            time.sleep(1)
            pg.doubleClick(x=346, y=319)
            pg.hotkey('ctrl', 'a')
            digitar(codigo)
            pg.press('enter')
            choice = pg.confirm('Escolha a peça, copie o código interno e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
            if choice == 'Peça Indisponível':
                pyperclip.copy('Indisponível')
            else:
                pg.press('home')
                time.sleep(1)
                pg.doubleClick(x=346, y=319)
                pg.hotkey('ctrl', 'a')
                pg.hotkey('ctrl', 'v')
                pg.press('enter')
                time.sleep(1.5)
                pg.click(x=901, y=329)
                for c in range(0,3):
                    pg.press('down')
                pg.doubleClick(x=788, y=705)
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
    
            # quit()