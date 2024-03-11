from defs import *
from interface.menu import menu
import pyautogui as pg
import pyperclip

# pg.FAILSAFE = True

# produtos = menu()
produtos = [['sk421', 'sp271', 'w6110'], ['t36083', 'vkm4790', 'ph2966'], ['wo1']]
codigo = str(produtos[0][0])

#abrir o chrome
pg.hotkey('win', 'r')
time.sleep(0.25)
digitar('chrome')
pg.press('enter')
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\nova_guia.png')#C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\nova_guia.png
pg.hotkey('win', 'up')
abrir_site('peca.ai')

#pesquisa peca.ai
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_peca.ai.png')
clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\busca_peca.ai.png')
pg.press('tab')
digitar(codigo)
try:
    login = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\logado_peca.ai.png')
except pg.ImageNotFoundException:
    pg.press('enter')
    time.sleep(1)
    for c in range (0, 3):
        pg.press('tab')
    pg.press('enter')
else:
    pg.press('enter')
time.sleep(1.5)

while True:
    try:
        sem_resultado = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\sem_resultado_peca.ai.png')
    except pg.ImageNotFoundException:
        break
    else:
        pg.press('f5')
        time.sleep(1.5)

while True:
    try:
        indisponivel = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\indisponivel_peca.ai.png')
    except pg.ImageNotFoundException:

        #PROCESSO MANUAL PECA.AI
        choice = pg.confirm('Escolha a peça e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
        if choice == 'Peça Indisponível':
            pyperclip.copy('Indisponível')
            break
        time.sleep(0.5)
        enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\comprar_peca.ai.png')
        pg.click(x=151, y=651)
        pg.click(x=151, y=651)
        pg.hotkey('ctrl', 'c')
        unformat()
        break
    else:
        pyperclip.copy('Indisponível')
        break

# abrir o excel
time.sleep(0.5)
pg.hotkey('win', 'r')
time.sleep(0.2)
pg.write('excel')
pg.press('enter')
time.sleep(2)
# enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_excel.png')
pg.hotkey('win', 'up')
pg.press('tab')
pg.press('tab')
pg.write('Planilha de Base para Cotacao')
time.sleep(0.5)
pg.press('enter')
time.sleep(2)

#excel peca.ai
escrever_celula('b2', codigo)
pg.click(x=56, y=181)
pg.click(x=56, y=181)
pg.write('c2')
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
pg.doubleClick(x=307, y=247)
pg.click(x=307, y=247)
pg.hotkey('ctrl', 'c')
text = pyperclip.paste().split('-')[0]
alttab()
colar_celula('a2', text)

#pesquisa mecanizou
alttab()
pg.hotkey('ctrl', 't')
abrir_site('app.mecanizou.com')
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
    clickar_imagem(r'imagens/sifrao_mecanizou.png', 3)
    pg.hotkey('ctrl', 'c')
    pyperclip.copy(pyperclip.paste()[3:])

#excel mecanizou
alttab()
pg.click(x=56, y=181)
pg.write('d2')
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
pg.hotkey('ctrl', 't')
abrir_site('https://peca.compel.com.br/')
time.sleep(1)
try:
    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\acessar_compel.png')
except pg.ImageNotFoundException:
    pass
else:
    pg.click(x=1248, y=366)
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\enquantonao_compel2.png')
pg.click(x=404, y=417)
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
pg.write('e2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+10')
    pg.press('enter')

#dpk pesquisa
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://www.kdapeca.com.br/login')
time.sleep(3.5)
pg.doubleClick(x=1166, y=709)
time.sleep(1)
pg.press('esc')
time.sleep(0.5)
pg.click(x=314, y=326)
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
pg.write('f2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+10')
    pg.press('enter')

#pesquisa rmp
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://loja.rmp.com.br/')
pg.click(x=285, y=138)
pg.write(codigo)
time.sleep(0.5)
pg.press('enter')
choice = pg.confirm('Escolha a peça e depois clique no título.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

if choice == 'Ok':
    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\sifrao_rpm.png', 3)
    pg.hotkey('ctrl', 'c')
    pyperclip.copy(pyperclip.paste()[2:])
else:
    pyperclip.copy('Indisponível')


#excel rmp
alttab()
pg.click(x=56, y=181)
pg.click(x=56, y=181)
pg.write('g2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+40')
    pg.press('enter')

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
                time.sleep(0.5)
                pg.click(x=0, y=371)
                pg.press('home')
                time.sleep(0.3)
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
                    clickar_imagem(r'imagens/sifrao_mecanizou.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[3:])

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

                #pesquisa rmp
                alttab()
                pg.hotkey('ctrl', '5')
                pg.click(x=285, y=138)
                pg.hotkey('ctrl', 'a')
                pg.write(codigo)
                time.sleep(0.5)
                pg.press('enter')
                choice = pg.confirm('Escolha a peça e depois clique no título.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

                if choice == 'Ok':
                    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\sifrao_rpm.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[2:])
                else:
                    pyperclip.copy('Indisponível')
                

                #excel rmp
                alttab()
                pg.click(x=56, y=181)
                pg.click(x=56, y=181)
                pg.write('g' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+40')
                    pg.press('enter')

                #indice increase
                celula_peca = 5
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
                time.sleep(0.5)
                pg.click(x=0, y=371)
                pg.press('home')
                time.sleep(0.3)
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
                    clickar_imagem(r'imagens/sifrao_mecanizou.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[3:])

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

                #processo rmp
                alttab()
                pg.hotkey('ctrl', '5')
                pg.click(x=285, y=138)
                pg.hotkey('ctrl', 'a')
                pg.write(codigo)
                time.sleep(0.5)
                pg.press('enter')
                choice = pg.confirm('Escolha a peça e depois clique no título.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

                if choice == 'Ok':
                    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\sifrao_rpm.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[2:])
                else:
                    pyperclip.copy('Indisponível')
                

                #excel rmp
                alttab()
                pg.click(x=56, y=181)
                pg.click(x=56, y=181)
                pg.write('g' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+40')
                    pg.press('enter')

                #indice increase
                celula_excel += 1
    else:
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
            time.sleep(0.5)
            pg.click(x=0, y=371)
            pg.press('home')
            time.sleep(0.3)
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
                clickar_imagem(r'imagens/sifrao_mecanizou.png', 3)
                pg.hotkey('ctrl', 'c')
                pyperclip.copy(pyperclip.paste()[3:])

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

            #processo rmp
            alttab()
            pg.hotkey('ctrl', '5')
            pg.click(x=285, y=138)
            pg.hotkey('ctrl', 'a')
            pg.write(codigo)
            time.sleep(0.5)
            pg.press('enter')
            choice = pg.confirm('Escolha a peça e depois clique no título.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

            if choice == 'Ok':
                clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\hawks-automations\imagens\sifrao_rpm.png', 3)
                pg.hotkey('ctrl', 'c')
                pyperclip.copy(pyperclip.paste()[2:])
            else:
                pyperclip.copy('Indisponível')
            

            #excel rmp
            alttab()
            pg.click(x=56, y=181)
            pg.click(x=56, y=181)
            pg.write('g' + str(celula_excel))
            pg.press('enter')
            if str(pyperclip.paste()) == 'Indisponível':
                pg.hotkey('ctrl', 'v')
            else:
                pg.write('=')
                pg.hotkey('ctrl', 'v')
                pg.write('+40')
                pg.press('enter')

            #indice increase
            celula_excel += 1

    if peça != produtos[0]:
        celula_peca += 3
