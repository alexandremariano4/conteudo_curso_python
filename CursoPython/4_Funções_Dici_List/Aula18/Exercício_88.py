from random import randint
from time import sleep
jogos = list()
lista = []
print('='*50)
print('{:=^50}'.format(f'JOGA NA MEGA SENA'))
print('='*50)
quant = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' *3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {i+1}: {l}')
print('-='*5,'Boa sorte!!!', '=-'*5)
