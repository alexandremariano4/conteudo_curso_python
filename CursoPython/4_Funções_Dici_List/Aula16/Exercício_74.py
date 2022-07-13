from random import randint

tupla = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
for n in tupla:
    print(n,end=' ')
print('\nMenor número: ',max(tupla))
print('Maior número: ',min(tupla))