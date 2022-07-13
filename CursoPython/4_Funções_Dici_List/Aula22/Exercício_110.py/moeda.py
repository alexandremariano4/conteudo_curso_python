def aumentar(preço=0,taxa=0,formato=False):
    res = preço+(preço*taxa/100)
    return res if format is False else formatar(res)
    
    
def diminuir(preço=0,taxa=0,formato=False):
    res = preço-(preço*taxa/100)
    return res if formato is False else formatar(res)
    
    
def dobro(preço=0,formato=False):
    res = preço*2
    return res if not formato else formatar(res)
    
    
def metade(preço=0,formato=False):
    res = preço/2
    return res if not formato else formatar(res)

def formatar(preço=0,moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço=0,taxaA=10,taxaR=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado:      \t{formatar(preço)}')
    print(f'Dobro do preço:       \t{dobro(preço,True)}')
    print(f'Metade do preço:      \t{metade(preço,True)}')
    print(f'{taxaA}% de aumento:  \t{aumentar(preço,taxaA,True)} ')
    print(f'{taxaR}% de redução:  \t{diminuir(preço,taxaR,True)}')
    print('-'*40)
    
    