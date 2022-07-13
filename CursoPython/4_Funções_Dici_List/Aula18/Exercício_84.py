dados = []
individual = []
pesado = leve = 0
magro = []
gordo = []
while True:
    #Contagem de pessoas cadastradas

 
    #Recebe na lista individual e insere a cópia no dados
    individual.append(str(input('Nome: ')))
    individual.append(int(input('Peso: ')))
    
    if len(dados) == 0:
        pesado = leve = individual[1]
    else:
        if individual[1] > pesado:
            pesado = individual[1]
        if individual[1] < leve:
            leve = individual[1]

    dados.append(individual[:])
    #Apaga a lista individual enquanto a lista de dados já está com os dados copiados
    individual.clear()
    #Recebe a opção se o usuário quer ou não continuar.
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SsNn':
        opcao = str(input('Digite uma opção válida [S/N] ')).upper().strip()[:]
        if opcao == 'N':
            break
    if opcao == 'N':
        print('='*40)
        print('Fim do programa...')
        break
    #Fim da estrutura de validação para encerrar programa

print(f'O maior peso é {pesado}Kg. Peso de ',end=' ')
for pessoas in dados:
    if pessoas[1] == pesado:
        print(f'[{pessoas[0]}]',end=' ')
print(f'O menor peso é {leve}Kg. Peso de ',end=' ')   
for pessoas in dados:
    if pessoas[1] == leve:
        print(f'[{pessoas[0]}]',end=' ')         


print(f'\033[1;31m{len(dados)} Pessoas foram cadastradas...\033[m')
