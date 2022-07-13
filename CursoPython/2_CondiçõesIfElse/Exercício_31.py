dist = int(input('Qual a distância que você irá viajar em km: '))
if dist < 200:
    print('Sua viagem ficará no valor de: R${}'.format(dist*0.50))
else:
    print('Sua viagem ficará no valor de: R${}'.format(dist*0.45))