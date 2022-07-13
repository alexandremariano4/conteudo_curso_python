from random import randint

print('-=-'*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*30)
cont = 0
vit = 0
while True:
    cont = cont +1
    computador = randint(1,10)
    jogador = int(input('Jogue um número: '))
    escolha = str(input('Par ou Ímpar: ')).upper().strip()[0]
    while escolha not in 'PpIi':
            escolha = str(input('Par ou Ímpar: ')).upper().strip()[0]
    resultado = computador + jogador
    if resultado % 2 == 0:
        print('--'*30)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU PAR!!!')
        print('--'*30)
        if escolha == 'P':
            print('Você \033[1;32mVENCEU!!!\033[m')
            vit = vit +1
        else:
            print('Você \033[1;31mPERDEU!!!\033[m')
            break
    else:
        print('--'*30)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU IMPAR!!!')
        print('--'*30)
        if escolha == 'I':
            print('Você \033[1;32mVENCEU!!!\033[m')
            vit = vit +1
        else:
            print('Você \033[1;31mPERDEU!!!\033[m')
            break
if vit % 2 == 0:
    print(f'GAME OVER!!! Você venceu {vit} vezes!!!')
else:
    print(f'GAME OVER!!! Você venceu {vit} vez!!!')