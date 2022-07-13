def fatorial(num=1):
    f = 1 
    for c in range(num,0,-1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')


def par(n=0):
    retorno = {True: 'Par', False: 'Impar'}
    if n==0:
        return 'Valor zero'
    if n%2==0:
        return retorno[True]
    else:
        return retorno[False]


num = int(input('Digite um número: '))
print(par(num))