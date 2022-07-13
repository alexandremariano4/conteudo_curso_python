from random import randint
from time import sleep

num = randint(0,5)
print('-=-' * 30)
print('Bem vindo ao jogo de adivinhação!')
print('-=-' * 30)
n1 = int(input('Digite um valor de 0 a 5 para ver se acertou o número!: '))
print('PROCESSANDO!!!')
sleep(2)
if num == n1:
    print(f'Você acertou! O número gerado foi {num}')
elif n1 > 5:
    print('Digite um número entre 0 e 5!')
else:
    print(f'Você errou! O número gerado foi {num}')
