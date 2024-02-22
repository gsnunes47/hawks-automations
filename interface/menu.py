# import pyautogui as pg
import pymsgbox as pg
# def pegar_codigos():


pg.CANCEL_TEXT = 'Finalizar'
pg.OK_TEXT = 'Próximo'
cont_peca = 1 
cont_code = 1
produtos = []

while True:

    #adicionar peças
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
    
    #formatação de texto
    txt = ''
    pg.CANCEL_TEXT = 'Cancelar'
    pg.OK_TEXT = 'Ok'
    
    while True:

        # formatação da lista
        for indice, peca in enumerate(produtos):
            if len(peca) == 0:
                produtos.pop(indice)

        #formatação de texto
        txt = ''
        for indice, peca in enumerate(produtos):
            txt += f'''Peça {indice + 1} - {peca}
'''
        escolha = pg.confirm(f'''Peças cotadas:
{txt}''', buttons=['Continuar', 'Adicionar mais peças', 'Excluir Peça', 'Corrigir'], title='Cotação RPA') #ADICIONAR MAIS PEÇAS
        if escolha == 'Corrigir':
            #pegar peca a ser corrigida
            while True:
                try:
                    peca = int(pg.password(f'''Peças cotadas:
{txt}
Qual peça você deseja corrigir os códigos? (Digite apenas o número)''', title='Cotação RPA', mask='')) - 1
                    codigo_corrigido = produtos[peca]
                except ValueError:
                    pg.alert('Insira um valor numérico!')
                    continue
                except IndexError:
                    pg.alert(f'Não há peça {peca + 1}!')
                    continue
                else:
                    break
            
            if len(produtos[peca]) == 3:
                escolha = 'Alterar código'
            else:
                escolha = pg.confirm(f'Peça {peca + 1} - {produtos[peca]}', buttons=['Alterar código', 'Adicionar código'])

            if escolha == 'Alterar código':
                # pegar codigo a ser corrigido
                while True:
                    try:
                        code = int(pg.password(f'''Qual código você deseja corrigir? (Digite apenas o número)
    {produtos[peca]}''', title='Cotação RPA', mask='')) - 1
                        codigo_corrigido = codigo_corrigido[code]
                    except ValueError:
                        pg.alert('Insira um valor numérico!')
                        continue
                    except IndexError:
                        pg.alert(f'Não há codigo {code + 1}!')
                        continue
                    else:
                        break

                new_code = pg.password(f'{codigo_corrigido}', title='Cotação RPA', mask='')
                if new_code:
                    produtos[peca][code] = new_code
                continue
                
            else:
                new_code = pg.password('Digite o novo código.', title='Cotação RPA', mask='')
                if new_code:
                    produtos[peca].append(new_code)
                continue

        elif escolha == 'Adicionar mais peças':
            break
        
        elif escolha == 'Excluir Peça':
            #pegar peca a ser corrigida
            while True:
                try:
                    peca = int(pg.password(f'''Peças cotadas:
{txt}
Qual peça você deseja excluir? (Digite apenas o número)''', title='Cotação RPA', mask='')) - 1
                    codigo_corrigido = produtos[peca]
                except ValueError:
                    pg.alert('Insira um valor numérico!')
                    continue
                except IndexError:
                    pg.alert(f'Não há peça {peca + 1}!')
                    continue
                else:
                    break
            produtos.pop(peca)
        
        else:
            #return
            print(produtos)
            quit()
        continue

print(produtos)





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