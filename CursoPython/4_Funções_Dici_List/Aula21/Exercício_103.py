def jogador(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))


if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    jogador(gols=gols)
else:
    jogador(nome,gols)
