lanche = ('Hamburguer','Suco','Pizza','Pudim')
print(lanche[::-1])
print(lanche[-2::])
print(lanche)

###Primeira maneira sem posição
for comida in lanche:
    print(f'Eu vou comer {comida}')
    
print('Quantidade de itens na tupla',len(lanche))
###Maneira precisando da posição
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
###Outra maneira precisando da posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')
###Sortear em ordem alfabética ou numérica
print(sorted(lanche))

teste = {1:'Teste',2:'Testudo'}
print(teste[1])