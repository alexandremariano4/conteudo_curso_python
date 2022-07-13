pares = list()
impares = list()
while True:
    numero = int(input('Digite um número: '))
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)
    opcao = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if 'N' in opcao:
        print('Fim do programa')
        break
lista = pares + impares
lista.sort()
print(f'Lista original: {lista}')
print(f'Lista pares: {pares}')
print(f'Lista impares: {impares}')