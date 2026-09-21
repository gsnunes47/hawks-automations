from defs import *
from interface.menu import menu
import pyautogui as pg
import pyperclip

pg.FAILSAFE = False

produtos = menu()
tem_nome = False
# produtos = [['sk421'], ['t36083'], ['vkm4790'], ['ph2966'], ['wo1']]#, 'sp271', 'w6110']]
codigo = str(produtos[0][0])

#abrir o chrome
pg.hotkey('win', 'r')
time.sleep(0.25)
digitar('chrome')
pg.press('enter')
time.sleep(1)
pg.hotkey('win', 'up')
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\nova_guia.png')#C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\nova_guia.png
abrir_site('fornecedor_a')

#pesquisa fornecedor_a
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_fornecedor_a.png')
clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\busca_fornecedor_a.png')
pg.press('tab')
digitar(codigo)
try:
    login = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\logado_fornecedor_a.png')
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
        sem_resultado = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sem_resultado_fornecedor_a.png')
    except pg.ImageNotFoundException:
        break
    else:
        pg.press('f5')
        time.sleep(1.5)

while True:
    try:
        indisponivel = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\indisponivel_fornecedor_a.png')
    except pg.ImageNotFoundException:

        #PROCESSO MANUAL fornecedor_a
        choice = pg.confirm('Escolha a peça e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
        if choice == 'Peça Indisponível':
            pyperclip.copy('Indisponível')
            break
        time.sleep(0.5)
        enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\comprar_fornecedor_a.png')
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
time.sleep(0.2)
pg.press('enter')
time.sleep(2)
# enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_excel.png')
pg.hotkey('win', 'up')
pg.press('tab')
pg.press('tab')
pg.write('Planilha de Base para Cotacao')
time.sleep(0.5)
pg.press('enter')
time.sleep(2)

#excel fornecedor_a
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
    pg.write('+12')
    pg.press('enter')
    tem_nome = pegar_nome_peca_ai(tem_nome, 'a2')

#pesquisa fornecedor_b
alttab()
pg.hotkey('ctrl', 't')
abrir_site('app.fornecedor_b.com')
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_fornecedor_b2.png')
pg.press('tab')
pg.write(codigo)
pg.click(x=1162, y=403)
while True:
    try:
        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marca_fornecedor_b.png')
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
    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_fornecedor_b.png', 3)
    pg.hotkey('ctrl', 'c')
    pyperclip.copy(pyperclip.paste()[3:])

#excel fornecedor_b
alttab()
pg.click(x=56, y=181)
pg.write('d2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+9')
    pg.press('enter')
    tem_nome = pegar_nome_fornecedor_b(tem_nome, '2a')

#fornecedor_c pesquisa
alttab()
pg.hotkey('ctrl', 't')
abrir_site('fornecedor.exemplo')
time.sleep(1)
try:
    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\acessar_fornecedor_c.png')
except pg.ImageNotFoundException:
    pass
else:
    pg.click(x=1248, y=366)
enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_fornecedor_c2.png')
pg.click(x=404, y=417)
digitar(codigo)
pg.press('enter')
time.sleep(3.5)

choice = pg.confirm('Escolha a peça, clique em detalhes e depois clique em OK.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')
if choice == 'Peça Indisponível':
    pyperclip.copy('Indisponível')
else:
    enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\preco_fornecedor_c.png')
    tem_nome = pegar_nome_fornecedor_c(tem_nome, 'a2')
    pg.doubleClick(x=701, y=339)
    pg.hotkey('ctrl', 'c')
    unformat()
    time.sleep(0.1)
    pg.click(x=1125, y=147)

#excel fornecedor_c
alttab()
pg.click(x=56, y=181)
pg.write('e2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+14')
    pg.press('enter')

#fornecedor_d pesquisa
alttab()
pg.hotkey('ctrl', 't')
abrir_site('fornecedor.exemplo')
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
    pg.click(x=0, y=303)
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

#excel fornecedor_d
alttab()
pg.click(x=56, y=181)
pg.write('f2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+14')
    pg.press('enter')
    tem_nome = pegar_nome_dpk(tem_nome, 'a2')

#pesquisa fornecedor_e
alttab()
pg.hotkey('ctrl', 't')
abrir_site('fornecedor.exemplo')

#verificação de login fornecedor_e
contador = 0
while True:
    try:
        if contador == 2:
            pg.moveTo(x=1355, y=135)
            time.sleep(0.5)
            pg.click(x=1244, y=524)
            time.sleep(3.5)
            break
        time.sleep(1)
        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\logado_rmp.png', grayscale=True, confidence=0.9)
    except pg.ImageNotFoundException:
        contador += 1
        continue
    else:
        break

pg.click(x=285, y=138)
pg.write(codigo)
time.sleep(0.5)
pg.press('enter')
choice = pg.confirm('Escolha a peça, clique no título, espere carregar o preço e clique em Ok.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

if choice == 'Ok':
    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_rpm.png', 3)
    pg.hotkey('ctrl', 'c')
    pyperclip.copy(pyperclip.paste()[2:])
else:
    pyperclip.copy('Indisponível')


#excel fornecedor_e
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
    pg.write('+35')
    pg.press('enter')
    tem_nome = pegar_nome_rmp(tem_nome, 'a2')

#markup
pg.doubleClick(x=56, y=181)
pg.write('$C$2:$G$2')
pg.press('enter')
pg.hotkey('ctrl', 'c')

teste = pyperclip.paste()

num = ''
num_list = []
final_list = []
for c in teste:
    if c == ',':
        num += '.'
    elif c == '\t' or c == '\n':
        if c == teste[0]:
            continue
        else:
            num_list.append(num)
            num = ''
    elif c == '\r':
        continue
    else:
        num += c

for i, v in enumerate(num_list):
    if v != 'Indisponível':
        final_list.append(float(v))

try:
    celula = f'{(sum(final_list) / len(final_list)) * 1.6:.2f}'
except ZeroDivisionError:
    pass
else:
    pg.doubleClick(x=56, y=181)
    pg.write('h2')
    pg.press('enter')
    pyperclip.copy(celula)
    pg.hotkey('ctrl', 'v')
pg.press('esc')

celula_peca = 2
for peça in produtos:
    tem_nome = False
    celula_excel = celula_peca
    if peça == produtos[0]:
        celula_peca = 3
        celula_excel = celula_peca
        for codigo in peça:
            if codigo == peça[0]:
                celula_peca = 5
                pass
            elif codigo == peça[-1]:

                # precesso fornecedor_a
                alttab()
                pg.hotkey('ctrl', '1')
                while True:
                    try:
                        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
                    except pg.ImageNotFoundException:
                        pg.hotkey('alt', 'left')
                        while True:
                            try:
                                img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
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
                    enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\comprar_fornecedor_a.png')
                    pg.click(x=151, y=651)
                    pg.click(x=151, y=651)
                    pg.hotkey('ctrl', 'c')
                    unformat()

                #excel fornecedor_a
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
                    pg.write('+12')
                    pg.press('enter')

                #processo fornecedor_b
                alttab()
                pg.hotkey('ctrl', '2')
                pg.hotkey('alt', 'left')
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_fornecedor_b2.png')
                pg.press('tab')
                pg.write(codigo)
                pg.click(x=1162, y=403)
                while True:
                    try:
                        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marca_fornecedor_b.png')
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
                    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_fornecedor_b.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[3:])

                #excel fornecedor_b
                alttab()
                pg.click(x=56, y=181)
                pg.write('d' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+9')
                    pg.press('enter')

                #processo fornecedor_c
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
                    enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\preco_fornecedor_c.png')
                    pg.doubleClick(x=701, y=339)
                    pg.hotkey('ctrl', 'c')
                    unformat()
                    time.sleep(0.1)
                    pg.click(x=1125, y=147)

                #excel fornecedor_c
                alttab()
                pg.click(x=56, y=181)
                pg.write('e' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+14')
                    pg.press('enter')

                #processo fornecedor_d
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

                #excel fornecedor_d
                alttab()
                pg.click(x=56, y=181)
                pg.write('f' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+14')
                    pg.press('enter')

                #pesquisa fornecedor_e
                alttab()
                pg.hotkey('ctrl', '5')
                pg.click(x=285, y=138)
                pg.hotkey('ctrl', 'a')
                pg.write(codigo)
                time.sleep(0.5)
                pg.press('enter')
                choice = pg.confirm('Escolha a peça, clique no título, espere carregar o preço e clique em Ok.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

                if choice == 'Ok':
                    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_rpm.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[2:])
                else:
                    pyperclip.copy('Indisponível')
                

                #excel fornecedor_e
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
                    pg.write('+35')
                    pg.press('enter')

                #markup
                pg.doubleClick(x=56, y=181)
                pg.write(f'$C${celula_excel}:$G${celula_excel}')
                pg.press('enter')
                pg.hotkey('ctrl', 'c')

                teste = pyperclip.paste()

                num = ''
                num_list = []
                final_list = []
                for c in teste:
                    if c == ',':
                        num += '.'
                    elif c == '\t' or c == '\n':
                        if c == teste[0]:
                            continue
                        else:
                            num_list.append(num)
                            num = ''
                    elif c == '\r':
                        continue
                    else:
                        num += c

                for i, v in enumerate(num_list):
                    if v != 'Indisponível':
                        final_list.append(float(v))

                try:
                    celula = f'{(sum(final_list) / len(final_list)) * 1.6:.2f}'
                except ZeroDivisionError:
                    pass
                else:
                    pg.doubleClick(x=56, y=181)
                    pg.write('h' + str(celula_excel))
                    pg.press('enter')
                    pyperclip.copy(celula)
                    pg.hotkey('ctrl', 'v')
                pg.press('esc')

                #indice increase
                celula_peca = 5
            else:
                # precesso fornecedor_a
                alttab()
                pg.hotkey('ctrl', '1')
                while True:
                    try:
                        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
                    except pg.ImageNotFoundException:
                        pg.hotkey('alt', 'left')
                        while True:
                            try:
                                img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
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
                    enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\comprar_fornecedor_a.png')
                    pg.click(x=151, y=651)
                    pg.click(x=151, y=651)
                    pg.hotkey('ctrl', 'c')
                    unformat()

                #excel fornecedor_a
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
                    pg.write('+12')
                    pg.press('enter')

                #processo fornecedor_b
                alttab()
                pg.hotkey('ctrl', '2')
                pg.hotkey('alt', 'left')
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_fornecedor_b2.png')
                pg.press('tab')
                pg.write(codigo)
                pg.click(x=1162, y=403)
                while True:
                    try:
                        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marca_fornecedor_b.png')
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
                    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_fornecedor_b.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[3:])

                #excel fornecedor_b
                alttab()
                pg.click(x=56, y=181)
                pg.write('d' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+9')
                    pg.press('enter')

                #processo fornecedor_c
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
                    enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\preco_fornecedor_c.png')
                    pg.doubleClick(x=701, y=339)
                    pg.hotkey('ctrl', 'c')
                    unformat()
                    time.sleep(0.1)
                    pg.click(x=1125, y=147)

                #excel fornecedor_c
                alttab()
                pg.click(x=56, y=181)
                pg.write('e' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+14')
                    pg.press('enter')

                #processo fornecedor_d
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

                #excel fornecedor_d
                alttab()
                pg.click(x=56, y=181)
                pg.write('f' + str(celula_excel))
                pg.press('enter')
                if str(pyperclip.paste()) == 'Indisponível':
                    pg.hotkey('ctrl', 'v')
                else:
                    pg.write('=')
                    pg.hotkey('ctrl', 'v')
                    pg.write('+14')
                    pg.press('enter')

                #processo fornecedor_e
                alttab()
                pg.hotkey('ctrl', '5')
                pg.click(x=285, y=138)
                pg.hotkey('ctrl', 'a')
                pg.write(codigo)
                time.sleep(0.5)
                pg.press('enter')
                choice = pg.confirm('Escolha a peça, clique no título, espere carregar o preço e clique em Ok.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

                if choice == 'Ok':
                    clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_rpm.png', 3)
                    pg.hotkey('ctrl', 'c')
                    pyperclip.copy(pyperclip.paste()[2:])
                else:
                    pyperclip.copy('Indisponível')
                

                #excel fornecedor_e
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
                    pg.write('+35')
                    pg.press('enter')

                #markup
                pg.doubleClick(x=56, y=181)
                pg.write(f'$C${celula_excel}:$G${celula_excel}')
                pg.press('enter')
                pg.hotkey('ctrl', 'c')

                teste = pyperclip.paste()

                num = ''
                num_list = []
                final_list = []
                for c in teste:
                    if c == ',':
                        num += '.'
                    elif c == '\t' or c == '\n':
                        if c == teste[0]:
                            continue
                        else:
                            num_list.append(num)
                            num = ''
                    elif c == '\r':
                        continue
                    else:
                        num += c

                for i, v in enumerate(num_list):
                    if v != 'Indisponível':
                        final_list.append(float(v))

                try:
                    celula = f'{(sum(final_list) / len(final_list)) * 1.6:.2f}'
                except ZeroDivisionError:
                    pass
                else:
                    pg.doubleClick(x=56, y=181)
                    pg.write('h' + str(celula_excel))
                    pg.press('enter')
                    pyperclip.copy(celula)
                    pg.hotkey('ctrl', 'v')
                pg.press('esc')

                #indice increase
                celula_excel += 1
    else:
        for codigo in peça:
            # precesso fornecedor_a
            alttab()
            pg.hotkey('ctrl', '1')
            while True:
                    try:
                        img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
                    except pg.ImageNotFoundException:
                        pg.hotkey('alt', 'left')
                        while True:
                            try:
                                img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
                            except pg.ImageNotFoundException:
                                continue
                            else:
                                break
                        break
                    else:
                        break
            time.sleep(0.5)
            pg.click(x=0, y=332)
            pg.press('home')
            while True:
                try:
                    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
                except pg.ImageNotFoundException:
                    pg.hotkey('alt', 'left')
                    while True:
                        try:
                            img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marcas_fornecedor_a.png')
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
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\comprar_fornecedor_a.png')
                pg.click(x=151, y=651)
                pg.click(x=151, y=651)
                pg.hotkey('ctrl', 'c')
                unformat()

            #excel fornecedor_a
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
                pg.write('+12')
                pg.press('enter')
                tem_nome = pegar_nome_peca_ai(tem_nome, celula='a' + str(celula_excel))

            #processo fornecedor_b
            alttab()
            pg.hotkey('ctrl', '2')
            pg.hotkey('alt', 'left')
            enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\enquantonao_fornecedor_b2.png')
            pg.press('tab')
            pg.write(codigo)
            pg.click(x=1162, y=403)
            while True:
                try:
                    img = pg.locateOnScreen(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\marca_fornecedor_b.png')
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
                clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_fornecedor_b.png', 3)
                pg.hotkey('ctrl', 'c')
                pyperclip.copy(pyperclip.paste()[3:])

            #excel fornecedor_b
            alttab()
            pg.click(x=56, y=181)
            pg.write('d' + str(celula_excel))
            pg.press('enter')
            if str(pyperclip.paste()) == 'Indisponível':
                pg.hotkey('ctrl', 'v')
            else:
                pg.write('=')
                pg.hotkey('ctrl', 'v')
                pg.write('+9')
                pg.press('enter')       
                tem_nome = pegar_nome_fornecedor_b(tem_nome, celula='a' + str(celula_excel))

            #processo fornecedor_c
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
                enquantonao(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\preco_fornecedor_c.png')
                tem_nome = pegar_nome_fornecedor_c(tem_nome, celula='a'+str(celula_excel))
                pg.doubleClick(x=701, y=339)
                pg.hotkey('ctrl', 'c')
                unformat()
                time.sleep(0.1)
                pg.click(x=1125, y=147)

            #excel fornecedor_c
            alttab()
            pg.click(x=56, y=181)
            pg.write('e' + str(celula_excel))
            pg.press('enter')
            if str(pyperclip.paste()) == 'Indisponível':
                pg.hotkey('ctrl', 'v')
            else:
                pg.write('=')
                pg.hotkey('ctrl', 'v')
                pg.write('+14')
                pg.press('enter')

            #processo fornecedor_d
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
                pg.click(x=0, y=303)
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

            #excel fornecedor_d
            alttab()
            pg.click(x=56, y=181)
            pg.write('f' + str(celula_excel))
            pg.press('enter')
            if str(pyperclip.paste()) == 'Indisponível':
                pg.hotkey('ctrl', 'v')
            else:
                pg.write('=')
                pg.hotkey('ctrl', 'v')
                pg.write('+14')
                pg.press('enter')
                tem_nome = pegar_nome_dpk(tem_nome, celula='a'+str(celula_excel))

            #processo fornecedor_e
            alttab()
            pg.hotkey('ctrl', '5')
            pg.click(x=285, y=138)
            pg.hotkey('ctrl', 'a')
            pg.write(codigo)
            time.sleep(0.5)
            pg.press('enter')
            choice = pg.confirm('Escolha a peça, clique no título, espere carregar o preço e clique em Ok.', buttons=['Ok', 'Peça Indisponível'], title='Cotação RPA')

            if choice == 'Ok':
                clickar_imagem(r'C:\Users\Dell\OneDrive\Documentos\GitHub\automacao-cotacao-pecas\imagens\sifrao_rpm.png', 3)
                pg.hotkey('ctrl', 'c')
                pyperclip.copy(pyperclip.paste()[2:])
            else:
                pyperclip.copy('Indisponível')
            

            #excel fornecedor_e
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
                pg.write('+35')
                pg.press('enter')
                tem_nome = pegar_nome_rmp(tem_nome, celula='a'+str(celula_excel))

            #markup
            pg.doubleClick(x=56, y=181)
            pg.write(f'$C${celula_excel}:$G${celula_excel}')
            pg.press('enter')
            pg.hotkey('ctrl', 'c')

            teste = pyperclip.paste()

            num = ''
            num_list = []
            final_list = []
            for c in teste:
                if c == ',':
                    num += '.'
                elif c == '\t' or c == '\n':
                    if c == teste[0]:
                        continue
                    else:
                        num_list.append(num)
                        num = ''
                elif c == '\r':
                    continue
                else:
                    num += c

            for i, v in enumerate(num_list):
                if v != 'Indisponível':
                    final_list.append(float(v))

            try:
                celula = f'{(sum(final_list) / len(final_list)) * 1.6:.2f}'
            except ZeroDivisionError:
                pass
            else:
                pg.doubleClick(x=56, y=181)
                pg.write('h' + str(celula_excel))
                pg.press('enter')
                pyperclip.copy(celula)
                pg.hotkey('ctrl', 'v')
            pg.press('esc')

            #indice increase
            celula_excel += 1

    if peça != produtos[0]:
        celula_peca += 3

pg.alert('Feito.', title='Cotações RPA')
