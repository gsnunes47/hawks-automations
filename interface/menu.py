# import pyautogui as pg
import pymsgbox as pg
# def pegar_codigos():


pg.CANCEL_TEXT = 'Finalizar'
pg.OK_TEXT = 'Próximo'
cont_peca = 1 
cont_code = 1
produtos = []
while True:
    # if len(produtos) < 1:
    while True:
        peça = []
        cont_code = 1
        while cont_code < 4:
            codigo = pg.password(f'Digite o {cont_code}º código da {cont_peca}ª peça', mask='', title='Cotação RPA') #FINISH
            if codigo == None:
                break
            peça.append(codigo)
            cont_code += 1
        produtos.append(peça)
        cont_peca += 1
        escolha = pg.confirm('Deseja continuar a adicionar peças?', buttons=['Sim', 'Não'], title='Cotação RPA')
        if escolha == 'Sim':
            continue
        else:
            break
    txt = ''
    pg.CANCEL_TEXT = 'Cancelar'
    pg.OK_TEXT = 'Ok'
    for indice, peca in enumerate(produtos):
        txt += f'''Peça {indice + 1} - {peca}
'''
    escolha = pg.confirm(f'''Peças cotadas:
{txt}''', buttons=['Continuar', 'Adicionar mais peças', 'Corrigir'], title='Cotação RPA') #ADICIONAR MAIS PEÇAS
    if escolha == 'Corrigir':
        peca = int(pg.password(f'''Peças cotadas:
{txt}
Qual peça você deseja corrigir os códigos? (Digite apenas o número)''', title='Cotação RPA', mask='')) - 1
        code = int(pg.password(f'''Qual código você deseja corrigir? (Digite apenas o número)
{produtos[peca]}''', title='Cotação RPA', mask='')) - 1
        new_code = pg.password(f'{produtos[peca][code]}', title='Cotação RPA', mask='')
        if new_code:
            produtos[peca][code] = new_code
        continue
    elif escolha == 'Adicionar mais peças':
        continue
    else:
        break





# return produtos







# escolha = pg.confirm('Bem vindo ao sistema de cotação RPA!, escolha com que modo você deseja continuar.', title='Cotação RPA', buttons=['Modo Automático', 'Modo com pausa'])
# if escolha == 'Modo com pausa':
#     modo = 'pause'
# else:
#     escolha = pg.confirm('ATENÇÃO!, tenha em mente que o modo automático ira pegar a primeira peça que aparecer no site ao pesquisar o código, mesmo que ela não seja a marca desejada.', buttons=['Continuar', 'Modo com pausa'], title='Cotação RPA')
#     if escolha == 'Continuar':
#         modo = 'auto'
#     else:
#         modo = 'pause'
        
# produtos = pegar_codigos()

# if modo == 'auto':
#     pass
# else:
#     pass