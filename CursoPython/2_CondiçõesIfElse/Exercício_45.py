from random import choice
from time import sleep

print('{:=^40}'.format(f'JO-KEN-PÔ!'))
jogador = int(input('''Faça sua escolha!!
{}1 - Pedra{}
{}2 - Papel{}
{}3 - Tesoura{}
Sua escolha: '''.format('\033[1;31m','\033[m','\033[1;32m','\033[m','\033[1;33m','\033[m')))
print('='*40)
if jogador != 1 and jogador != 2 and jogador != 3:
    print('Escolha uma opção válida, bocó!')
computador = choice(['Pedra','Papel','Tesoura'])
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
#jogador escolhe pedra
if jogador == 1 and computador == 'Pedra':
    print(f'Você escolheu Pedra e eu escolhi {computador}! \033[1;34mEMPATAMOS\033[m!!!')
elif jogador == 1 and computador == 'Papel':
    print(f'Você escolheu Pedra e eu escolhi {computador}! \033[1;32mEu venci\033[m!!!')
elif jogador == 1 and computador == 'Tesoura':
    print(f'Você escolheu Pedra e eu escolhi {computador}! \033[1;32mVocê venceu\033[m!!!')
#jogador escolhe papel
if jogador == 2 and computador == 'Papel':
    print(f'Você escolheu Papel e eu escolhi {computador}! \033[1;34mEMPATAMOS\033[m!!!')
elif jogador == 2 and computador == 'Tesoura':
    print(f'Você escolheu Papel e eu escolhi {computador}! \033[1;32mEu venci\033[m!!!')
elif jogador == 2 and computador == 'Pedra':
    print(f'Você escolheu Papel e eu escolhi {computador}! \033[1;32mVocê venceu\033[m!!!')
#jogador escolhe tesoura
if jogador == 3 and computador == 'Tesoura':
    print(f'Você escolheu Tesoura e eu escolhi {computador}! \033[1;34mEMPATAMOS\033[m!!!')
elif jogador == 3 and computador == 'Pedra':
    print(f'Você escolheu Tesoura e eu escolhi {computador}! \033[1;32mEu venci\033[m!!!')
elif jogador == 3 and computador == 'Papel':
    print(f'Você escolheu Tesoura e eu escolhi {computador}! \033[1;32mVocê venceu\033[m!!!')

print('='*40)

##Outra forma de fazer
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0,2)
# print('O computador escolheu {}'.format(itens[computador]))