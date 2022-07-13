######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for p in range (0,partidas):
    gols.append(int(input(f'Quantos gols na partida {p+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = total = total + gols[p]

print('-='*20)
print(jogador)
print('-='*20)

for v,k in jogador.items():
    print(f'O campo {v} tem o valor {k} ')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for indice,gols in enumerate(jogador['gols']):
    print(f'=> Na partida {indice+1}, fez {gols} gols')
print(f'Foi um total de {jogador["total"]} gols')
