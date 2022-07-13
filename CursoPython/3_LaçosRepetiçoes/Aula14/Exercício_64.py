numero = qtd = soma = 0
while numero != 999:

    numero = int(input('Digite um número qualquer: '))
    if numero != 999:
        qtd += +1 
        soma = soma + numero 
print(f'O programa rodou {qtd} vezes e a soma entre todos números digitados é de {soma}')