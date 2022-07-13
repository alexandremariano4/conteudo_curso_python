calculadora ={'soma' : lambda x: x+x,
              'duplicar' : lambda x: x*x}
######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
soma  = calculadora['soma']
duplicar = calculadora['duplicar']
print(soma(6))
print(duplicar(6))

# print(calculadora.values())
# print(calculadora.keys())
# print(calculadora.items())
# locadora = []
# filme = {
#     'titulo':'Star Wars',
#     'ano':1977,
#     'diretor':'George Lucas'
# }
# for k , v in filme.items():
#     print(f'O {k} é {v}')

# # print(filme.values())
# # print(filme.keys())
# # print(filme.items())
# locadora.append(filme)
# print('\n',locadora)
