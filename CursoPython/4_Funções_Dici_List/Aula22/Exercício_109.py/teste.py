import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do {moeda.formatar(p)} é {moeda.metade(p,True)}.')
print(f'O dobro de {moeda.formatar(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13,True)}')