n = int(input('Qual o número que você quer a tabuada: '))
print('{:=^40}'.format(f'TABUADA do {n}'))
for c in range (1,10+1):
    resultado = n * c 
    print(f'{n}x{c}={resultado}')
print('='*40)
