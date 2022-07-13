def teste(b):
    global a
    print(f'Antes de alterar o A {a}')
    a = 8
    b += 4
    c = 2
    """ X é uma variável de escopo local"""
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


#Programa principal
a = 5
"""N é uma variável de escopo global"""
teste(a)
print(f'A fora vale {a}')

# print(f'B fora vale {b}')
# print(f'C fora vale {c}')