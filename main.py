from defs import *
import pyautogui as pg
import pyperclip

pg.FAILSAFE = True
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
codigo = 'sp271'

#abrir o chrome
pg.hotkey('win', 'r')
time.sleep(0.25)
digitar('chrome')
pg.press('enter') #arrumar o tab, por que as vezes a leticia despadroniza o chrome
time.sleep(1) # enquantonao(r'imagens/nova_guia.png')
pg.hotkey('win', 'up')
abrir_site('peca.ai')

#pesquisa peca.ai
time.sleep(3.5) # enquantonao(r'imagens/enquantonao_peca.ai.png')
clickar_imagem(r'imagens/busca_peca.ai.png')
pg.press('tab')
digitar(codigo)
try:
    login = pg.locateOnScreen(r'imagens/logado_peca.ai.png')
except pg.ImageNotFoundException:
    logado = False
    pg.press('enter')
    enquantonao(r'imagens/entrar_peca.ai.png')
    for c in range (0, 3):
        pg.press('tab')
    pg.press('enter')
else:
    logado = True
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

# abrir o excel
pg.hotkey('ctrl', 'shift', 'alt', 'win', 'x')
time.sleep(5)
pg.press('tab')
pg.press('tab')
pg.write('Planilha de Base para Cotacao')
time.sleep(1)
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

#pesquisa mecanizou
alttab()
pg.hotkey('ctrl', 't')
abrir_site('app.mecanizou.com')
time.sleep(2)
pg.press('tab')
digitar(codigo)
pg.press('enter')
enquantonao(r'imagens/enquantonao_mecanizou.png') #time.sleep(2.75)
pg.click(x=500, y=491)
time.sleep(0.5)
pg.click(x=1005, y=388)
pg.click(x=1005, y=388)
pg.hotkey('ctrl', 'c')
unformat()

#excel mecanizou
alttab()
pg.click(x=56, y=181)
pg.write('d2')
pg.press('enter')
pg.write('=')
pg.hotkey('ctrl', 'v')
pg.write('+7')
pg.press('enter')  

#compel pesquisa
alttab()
pg.hotkey('ctrl', 't')
abrir_site('https://peca.compel.com.br/')
time.sleep(4)
try:
    img = pg.locateOnScreen(r'imagens/acessar_compel.png')
except pg.ImageNotFoundException:
    pass
else:
    pg.click(x=1248, y=366)
time.sleep(4)
pg.click(x=404, y=417) #verificação
digitar(codigo)
pg.press('enter')
enquantonao(r'imagens/enquantonao_compel.png') #time.sleep(12)
pg.doubleClick(x=321, y=630)
pg.hotkey('ctrl', 'c')
unformat()

#excel compel
alttab()
pg.click(x=56, y=181)
pg.write('e2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponével':
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
time.sleep(5)
pg.doubleClick(x=458, y=496)
time.sleep(1)
pg.press('esc')
time.sleep(0.5)
pg.click(x=301, y=251)
digitar(codigo)
pg.press('enter')
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
pg.write('f2')
pg.press('enter')
if str(pyperclip.paste()) == 'Indisponível':
    pg.hotkey('ctrl', 'v')
else:
    pg.write('=')
    pg.hotkey('ctrl', 'v')
    pg.write('+10')
    pg.press('enter')


# #loop a partir do segundo código
# produtos[0].pop(0)
    
# peca_num = 3    
# for peça in produtos:
#     for codigo in peça:   
#         if peca_num == 1:
#             peca_num += 1
#             continue
#         alttab()

#         #pesquisa peca.ai
#         pg.hotkey('ctrl', '1')
#         pg.hotkey('alt', 'left')
#         for c in range(0, 8):
#             pg.press('tab')
#         pg.hotkey('ctrl', 'a')
#         digitar(codigo)
#         pg.press('enter')
#         time.sleep(3)
#         pg.click(x=560, y=690)
#         pg.press('enter')
#         time.sleep(2)
#         pg.click(x=151, y=651)
#         pg.click(x=151, y=651)
#         pg.hotkey('ctrl', 'c')
#         unformat()
#         alttab()

#         #excel peca ai
#         escrever_celula(cell=str('b' + str(peca_num)), txt=codigo)
#         pg.click(x=56, y=181)
#         pg.click(x=56, y=181)
#         pg.write('c' + str(peca_num))
#         pg.press('enter')
#         pg.write('=')
#         pg.hotkey('ctrl', 'v')
#         pg.write('+15')
#         pg.press('enter')
#         break
#     break
