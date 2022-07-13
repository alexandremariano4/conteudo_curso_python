from operator import contains


tupla = (int(input('Digite o primeiro valor: ')) 
,int(input('Digite o segundo valor: '))
,int(input('Digite o terceiro valor: '))
,int(input('Digite o quarto valor: ')))

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 está na posição {tupla.index(3)+1}') 
else:
    print('O número 3 não aparece na tupla!')
    
print('Os números pares digitados foram ',end='→ ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')


contains=contains(tupla,3)
print(contains)

    
    
    