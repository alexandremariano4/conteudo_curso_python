tupla = (str(input('Digite o nome do produto: ')),float(input('Digite o preço do produto anterior: ')),
         str(input('Digite o nome do produto: ')),float(input('Digite o preço do produto anterior: ')),
         str(input('Digite o nome do produto: ')),float(input('Digite o preço do produto anterior: ')),
         str(input('Digite o nome do produto: ')),float(input('Digite o preço do produto anterior: ')),
         str(input('Digite o nome do produto: ')),float(input('Digite o preço do produto anterior: ')))

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}',end='')
    else:
        print(f'R${tupla[pos]:>5.2f}')