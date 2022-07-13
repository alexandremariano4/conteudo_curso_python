times = ('Palmeiras','Atlético','Corínthians',
         'Coritiba','São Paulo','Athletico-PR','Botafogo',
         'Flamengo','Santos','América-MG')

print('Cinco primeiros: ',times[0:5])
print('Últimos quatro: ',times[-4:])
print(f'Times em ordem alfabética: {sorted(times)}')
print('O Coritiba está na {}º posição'.format(times.index('Coritiba')+1))