def leitura(numero):
    while numero.isnumeric() != True:
        print('\033[1;31m ERRO! Digite um número inteiro válido.\033[m')
        numero = str(input('Digite um número: '))
    if numero.isnumeric() == True:
        print(f'Você acabou de digitar o número {numero}')
        print(f'O tipo do número {numero} é {type(int(numero))}')

n = str(input('Digite um número: '))
leitura(n)
