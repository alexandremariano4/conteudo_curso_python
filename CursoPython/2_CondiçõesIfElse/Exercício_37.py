numero = int(input('Digite um número para conversão: '))
opcao = int(input('Qual opção você deseja? \n1 - Binário\n2 - Octal\n3 - Hexadecimal\nSua opção: '))
if opcao == 1:
    binario = bin(numero)[2:]
    print('\033[1;33m',binario,'\033[m')
elif opcao == 2:
    octal = oct(numero)[2:]
    print('\033[1;32m',octal,'\033[m')
elif opcao == 3:
    hexa = hex(numero)[2:]
    print('\033[1;31m',hexa,'\033[m')
else:
    print('Digite uma opção válida!')