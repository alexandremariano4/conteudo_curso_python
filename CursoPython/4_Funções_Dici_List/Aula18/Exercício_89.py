notas = []
individual = []
cont = 0
media = []
while True:
    cont +=1
    individual.append(str(input('Nome: ')))
    individual.append(float(input('Nota 1: ')))
    individual.append(float(input('Nota 2: ')))
    individual.append((individual[1]+individual[2])/2)
    notas.append(individual[:])
    individual.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-='*30)
        
    while opcao not in 'nNsS':
        opcao = str(input('Digite uma opção válida? [S/N] ')).strip().upper()[0]
        if opcao in 'nN':
            break
    if opcao in 'nN':
            break
    
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>5}')
print('-'*30)

for i, l in enumerate(notas):
    print(f'{i:<4}  {l[0]:<10}      {l[3]:>8}')
print('-'*30)
while cont != 999:
    cont = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if cont == 999:
        break
    print(f'Notas de {notas[cont][0]} são {notas[cont][1:3]}')
    
