cont = 0
n1 = int(input('Digite o número para verificar se ele é um número primo: '))
for c in range (1, n1 +1):
    if n1 % c == 0:
        print('\033[33m', end='')
        cont += +1        
    else:
        print('\033[31m', end='')
    print('{} '.format(c),'\033[m', end='')
if cont == 2:
    print(f'\n{n1} Foi dividido {cont} vezes, ele é um número primo!')
else:
    print(f'\n{n1} Foi dividido {cont} vezes, ele não é um número primo!')
