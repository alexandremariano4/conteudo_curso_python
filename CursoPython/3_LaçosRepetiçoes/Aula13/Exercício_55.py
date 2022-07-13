maior = 0
menor = 0
for c in range (0,5):
    peso = float(input(f'Digite o peso da {c+1}ª pessoa: '))
    
    if c == 0:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso informado é {}, e o menor peso informado é {}'.format(maior,menor))