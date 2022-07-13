c = 1 
pares = impares = 0
while c != 0:
    c = int(input('Digite um valor: '))
    if c != 0:
        if c % 2 == 0:
            pares = pares +1
        else:
            impares = impares +1
print(f'Foram inseridos {pares} números pares e {impares} números impares.')
print('Fim')