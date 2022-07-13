a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(sorted(c))
print(len(c))
print('Quantas vezes aparece o número 5 :',c.count(5))
print('Que posição está o 5: ',c.index(5))
print('Que posição está o 5 a partir da posição 2: ',c.index(5,2))

pessoa = ('Alexandre', 39, 'M', 98.20)
#### Para apagar alguma coisa no python exemplo : del(pessoa)
print(pessoa)