maior = 0
menor = 0
for c in range (0,7):
    idade = int(input(f'Digite a {c+1}ª idade: '))
    if idade >= 21:
        maior = maior+1
    else:
        menor = menor+1
print(f'De todas idades inseridas, {menor} são menores de idade e {maior} maiores de idade.')