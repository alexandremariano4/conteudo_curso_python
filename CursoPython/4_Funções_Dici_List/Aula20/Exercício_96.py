def calcArea(l,c):
    areaTotal = l*c
    print(f'A área de um terreno {l}x{c} é de {areaTotal}m².')    
    
print(' Controle de Terrenos ')
print('__'*20)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

calcArea(l=largura,c=comprimento)