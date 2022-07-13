from math import factorial


def fatorial(n, show=True):
    c = n
    f = 1
    
    if show==True:
        print(f'Calculando {n}! = ', end='')
        while c > 0:
            print('{}'.format(c), end='')
            print(' x ' if c > 1 else ' = ', end='')
            f = f * c
            c = c - 1
        print('O fatorial de {} é {}'.format(n,f))
    else:
        print(factorial(n))

dic = {'S': True, 'N': False}
n = int(input('Digite um número: '))
show = str(input('Deseja visualizar o cálculo do fatorial: [S/N] ')).upper().strip()[0]
fatorial(n,dic[show])

# def fatorial(n, show=False):

#     f = 1
#     for c in range(n,0,-1):
#         if show:
#             print(c,end='')
#             if c>1:
#                 print(' x ', end='')
#             else:
#                 print(' = ',end='')
#         f *= c
#     return f
# print(fatorial(5,show=True))