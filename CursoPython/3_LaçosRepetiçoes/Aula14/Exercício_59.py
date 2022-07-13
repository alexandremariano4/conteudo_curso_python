from time import sleep


cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'roxo': '\033[1;35m',
         'limpa': '\033[m'}
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
texto = {1:'Somar os números',
         2:'Multiplicar os números',
         3:'Mostrar o maior número',
         4:'Preencher novos números'}
while opcao != 5:
    print('='*30)
    opcao = int(input('''[1] Somar os números
[2] Multiplicar os números
[3] Me mostre o maior número
[4] Preencher novos números
[5] Sair do programa\n\nSua opção: '''))
    if opcao == 1:
        print(f'Você escolheu a opção {opcao} ==> {texto[opcao]}')
        sleep(1)
        print(f'{cores["azul"]}PROCESSANDO!!!{cores["limpa"]}')
        sleep(1)
        print(f'A soma entre {cores["amarelo"]}{n1}{cores["limpa"]} e {cores["vermelho"]}{n2}{cores["limpa"]} é de {cores["roxo"]}{n1+n2}{cores["limpa"]}')
        sleep(2)
    elif opcao == 2:
        print(f'Você escolheu a opção {opcao} ==> {texto[opcao]}')
        sleep(1)
        print(f'{cores["azul"]}PROCESSANDO!!!{cores["limpa"]}')
        sleep(1)
        print(f'A multiplicação entre {cores["amarelo"]}{n1}{cores["limpa"]} e {cores["vermelho"]}{n2}{cores["limpa"]} é de {cores["roxo"]}{n1*n2}{cores["limpa"]}')
        sleep(2)
    elif opcao == 3:
        print(f'Você escolheu a opção {opcao} ==> {texto[opcao]}')
        sleep(1)
        print(f'{cores["azul"]}PROCESSANDO!!!{cores["limpa"]}')
        sleep(1)
        maior = n1 > n2
        if maior == True:
            print(f'O maior número entre {cores["amarelo"]}{n1}{cores["limpa"]} e {cores["vermelho"]}{n2}{cores["limpa"]} é {cores["roxo"]}{n1}{cores["limpa"]}')
        elif n1 == n2:
            print('Os números são iguais!!!')
        else:
            print(f'O maior número entre {cores["amarelo"]}{n1}{cores["limpa"]} e {cores["vermelho"]}{n2}{cores["limpa"]} é {cores["roxo"]}{n2}{cores["limpa"]}')
        sleep(2)
    elif opcao == 4:
        print(f'Você escolheu a opção {opcao} ==> {texto[opcao]}')
        sleep(1)
        print(f'{cores["azul"]}PROCESSANDO!!!{cores["limpa"]}')
        sleep(1)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        sleep(0.5)
        print(f'Agora o primeiro número é {n1} e o segundo número é {n2}.')     
        sleep(2)
    elif opcao == 5:
        print('Até a próxima!')
    else:
        print('Digite uma opção válida!!!')