from random import randint
from time import sleep
from operator import itemgetter
######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = []
print('Valores sorteados: ')

# com enumarete ele pega o Index e todo conteúdo daquele index, sem o enumarete (usando só jogo.items())
# ele pega respectivamente o nome do dicionário e o conteúdo dentro do dicionário na posição respectiva
for k,v in jogo.items():
    print(f'{k} tirou o número {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('== Ranking dos jogadores ==')
for i,r in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º LUGAR => {r[0]} com {r[1]}')
# jogadores = {}
# resultados = []
# dados = []

# for j in range (0,4):
#     jogadores['dado'] = randint(1,6)
#     while jogadores in resultados:
#         jogadores['dado'] = randint(1,6)
#     resultados.append(jogadores.copy())
#     jogadores.clear()
    
# for i in range (0,len(resultados)):
#     dados.append(resultados[i]['dado'])
# dados.sort()

# print('Valores sorteados: ')
# for i,r in enumerate(dados):
#     print(f'O jogador {i+1} tirou {r}')
# print('Ranking dos jogadores')