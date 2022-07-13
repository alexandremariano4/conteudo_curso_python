valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite o {cont+1} valor: ')))
for c,v in enumerate(valores):
    print(f'Os valores são: {v} na posição {c+1}')
print('Fim da lista')
