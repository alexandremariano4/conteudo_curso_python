from datetime import datetime
from time import sleep

pessoa = {}

for c in range(0,1):
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Ano de nascimento: '))
    pessoa['idade'] = (datetime.now().year) - pessoa['idade']
    pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if pessoa['ctps'] == 0:
        print(f'''Nome: {pessoa["nome"]}
Idade: {pessoa["idade"]}
CTPS: {pessoa["ctps"]}
Você não tem Carteira de trabalho!!!''')    
        break
        
    pessoa['AnoCont'] = int(input('Ano de contração: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['AnoCont'] + 35) - datetime.now().year)
    pessoa['salario'] = int(input('Salário: '))
    print('-='*40)
    sleep(1)
    print('PROCESSANDO...')
    sleep(1)
######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE


    print(f'''Nome: {pessoa["nome"]}
Idade: {pessoa["idade"]}
CTPS: {pessoa["ctps"]}
Contratação: {pessoa["AnoCont"]}
Salário: {pessoa["salario"]}
Aposentadoria: {pessoa["aposentadoria"]}''')