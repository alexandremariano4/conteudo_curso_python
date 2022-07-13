matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para ({l},{c}): '))
       
soma3C = 0
linha2 = 0
soma = 0

for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()

for l in range (0,3):
    for c in range (0,3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma dos valores pares é {soma}')
            
for c in range(0,3):
        soma3C += matriz[c][2]
print(f'A soma dos valores da terceira coluna é: {soma3C}')


for l in range(0,3):
        if l == 0:
            linha2 = matriz[1][l]
        elif matriz[1][l] > linha2:
            linha2 = matriz[1][c]

print(f'O maior número da segunda linha é: {linha2}')
