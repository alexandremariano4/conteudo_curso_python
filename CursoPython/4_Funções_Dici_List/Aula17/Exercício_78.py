lista = list()
for cont in range (0,5):
    lista.append(int(input(f'Digite o valor na {cont+1}º posição: ')))
    
print(f'O maior valor foi {max(lista)} nas posições: ',end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i+1}...',end='')
print(f'\nO menor valor foi {min(lista)} nas posições: ',end='')        
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i+1}...',end='')


 