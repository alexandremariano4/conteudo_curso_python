pessoa = [[],[]]
cont = 0
for p in range (0,3):
    cont = cont +1
    pessoa[0].append(str(input('Digite seu nome: ')))
    pessoa[1].append(int(input('Digite sua idade: ')))

for pessoas in range (0,cont):
    print(f'\nNome: {pessoa[0][pessoas]}',end=' ')
    print(f'→ Idade: {pessoa[1][pessoas]}')