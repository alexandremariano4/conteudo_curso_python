from random import randrange


t1 = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão dessa PA: '))
decimo = t1 + (10-1) * ra
for c in range (t1,decimo + ra ,ra):
    print('{}'.format(c), end='-> ')
print('Acabou!')