from random import randint

somar = []
sortear = []

def sorteio():
    for num in range(0,5):
        sortear.append(randint(0,20))
    print(sortear)       
        
def soma():
    total = 0
    for num in sortear:
        if num % 2 == 0:
            total = total + num
    somar.append(total)
            

print('Sorteando 5 valores da lista: ',end=' ')    
sorteio()
soma()
print(f'Somando os valores pares da lista, temos {max(somar)}')





