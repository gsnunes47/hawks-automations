# Hawks Automations

> 🛠️ **Projeto aplicado** — automação RPA para pesquisa de peças, comparação de preços e cálculo de markup.

Ferramenta desenvolvida para auxiliar consultores no processo de cotação de peças automotivas.

A partir do código de uma peça, a automação realiza pesquisas em diferentes fornecedores, coleta os preços encontrados e consolida os resultados em uma planilha para auxiliar no cálculo do valor final de revenda.

O projeto surgiu da tentativa de automatizar um processo que até então exigia diversas pesquisas e operações manuais por parte do consultor.

## Como funciona

O fluxo da automação consiste em:

1. Receber o código da peça a ser pesquisada;
2. Identificar o estado atual da aplicação/tela;
3. Acessar os fornecedores necessários pelo navegador;
4. Verificar autenticação e realizar login quando necessário;
5. Pesquisar a peça pelo código;
6. Coletar os preços encontrados;
7. Consolidar os resultados;
8. Gerar uma planilha com os custos e cálculo de markup.

## Modos de automação

Durante o desenvolvimento, percebi que uma automação totalmente baseada em interface gráfica poderia se tornar frágil diante de situações como mudanças de resolução, zoom, posicionamento de elementos e resultados inesperados.

Por isso, o projeto passou a contar com duas abordagens:

### Full Auto

Executa o fluxo de pesquisa de forma automatizada, utilizando interação com mouse e teclado para navegar pelas interfaces.

### Assisted Search

Mantém a automação das tarefas repetitivas, mas permite intervenção do consultor em pontos que exigem decisão humana, como selecionar o resultado correto ou indicar que determinada peça não foi encontrada.

Essa abordagem reduz a dependência de uma automação visual completamente autônoma e torna o processo mais tolerante a situações inesperadas.

## Abordagens exploradas

Durante o desenvolvimento também foram realizados testes com **web scraping** como alternativa à automação da interface.

A abordagem mostrou limitações para o cenário do projeto, principalmente pela necessidade de autenticação e pelo acesso restrito aos portais B2B utilizados no processo.

Por isso, a solução principal seguiu utilizando automação RPA.

## Tecnologias

- Python
- PyAutoGUI
- Automação RPA
- Web Scraping
- Excel

## Status

📚 Projeto descontinuado / mantido como registro de experiência prática com automação.
