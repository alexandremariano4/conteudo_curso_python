from time import sleep

for c in range(6 , 0 , -1):
    print('Ah nem!',c -1)
print('FIM!!!')


for c in range(0 , 7 , 2):
    print('Ah nem!',c )
print('FIM!!!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i , f+1 , p):
    print(c)
    
s = 0
for c in range (0,2):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma dos números inseridos é de: {s}')
