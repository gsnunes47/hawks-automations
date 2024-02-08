import pyautogui as pg

def pegar_codigos():
    cont_peca = 1 
    cont_code = 1
    produtos = []
    while True:
        if len(produtos) < 1:
            while True:
                peça = []
                cont_code = 1
                while cont_code < 4:
                    codigo = pg.password(f'Digite o {cont_code}º código da {cont_peca}ª peça', mask='', title='Cotação RPA')
                    if codigo == None:
                        break
                    peça.append(codigo)
                    cont_code += 1
                produtos.append(peça)
                cont_peca += 1
                escolha = pg.confirm('Deseja continuar?', buttons=['Sim', 'Não'], title='Cotação RPA')
                if escolha == 'Sim':
                    continue
                else:
                    break
        escolha = pg.confirm(f'''Peças cotadas: {produtos}''', buttons=['Continuar', 'Corrigir'], title='Cotação RPA')
        if escolha == 'Corrigir':
            txt = ''
            for indice, peca in enumerate(produtos):
                txt += f'''Peça {indice + 1} - {peca}
'''
            peca = int(pg.password(f'''Peças cotadas:
{txt}
Qual peça você deseja corrigir os códigos? (Digite apenas o número)''', title='Cotação RPA')) - 1
            code = int(pg.password(f'''Qual código você deseja corrigir? (Digite apenas o número)
{produtos[peca]}''', title='Cotação RPA')) - 1
            produtos[peca][code] = pg.password(f'{produtos[peca][code]}', title='Cotação RPA')
            continue
        else:
            break
    return produtos

# escolha = pg.confirm('Bem vindo ao sistema de cotação RPA!, escolha com que modo você deseja continuar.', title='Cotação RPA', buttons=['Modo Automático', 'Modo com pausa'])
# if escolha == 'Modo com pausa':
#     modo = 'pause'
# else:
#     escolha = pg.confirm('ATENÇÃO!, tenha em mente que o modo automático ira pegar a primeira peça que aparecer no site ao pesquisar o código, mesmo que ela não seja a peça desejada.', buttons=['Continuar', 'Modo com pausa'], title='Cotação RPA')
#     if escolha == 'Continuar':
#         modo = 'auto'
#     else:
#         modo = 'pause'
# print(modo)
produtos = pegar_codigos()
# print(produtos)
if modo == 'auto':
    pass
else:
    pass