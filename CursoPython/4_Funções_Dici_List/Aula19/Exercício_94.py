######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
pessoa = []
media = 0
mulheres = []
acima = []
while True:
    individual = {
        'nome' : str(input('Nome: ')),
        'sexo' : str(input('Sexo: ')).upper().strip()[0],
        'idade': int(input('Idade: '))
    }
    while individual['sexo'] not in 'FM':
        individual['sexo'] = str(input('ERRO! Digite um valor válido [M/F]: ')).upper().strip()[0]
    
    if individual['sexo'] == 'F':
        mulheres.append(individual['nome'])
        
    media = media + individual['idade']
    
    pessoa.append(individual.copy())
    individual.clear()
    
    
    print('-='*20)
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'sSnN':
        opcao = str(input('Digite uma opção válida [S/N] ')).upper().strip()[0]
    if opcao in 'nN':
        break

print('-='*20)
print(f'- O grupo tem {len(pessoa)} pessoas')
print(f'- A média de idade é de {media/len(pessoa):.2f}')
print(f'- As mulheres cadastradas foram: ',end='')

for m in mulheres:
    print(f'{m}',end=' ')
    
print('\n- Lista das pessoas que estão com a idade acima da média: ')
for p in pessoa:
    if p['idade'] >= media/len(pessoa):
        print(f'Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')
print('<<<ENCERRADO>>>')