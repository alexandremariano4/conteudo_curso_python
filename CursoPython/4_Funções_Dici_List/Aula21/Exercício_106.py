opcao = 'kek'
while opcao != 'fim':
    print('\033[1;35m-='*30)
    print(' Sistema de ajuda PyHelp')
    print('-='*30,'\033[m')
    opcao = str(input('Função ou Biblioteca >  '))
    
    print(help(opcao))

    
print('\033[1;31;41m-='*5)
print(' ATÉ LOGO  ')
print('-='*5,'\033[m')