estado = dict()
brasil = list()
######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
# for e in brasil:
#     for k,v in e.items():
#         print(f'O campo {k} tem valor {v}')


for e in range(0,len(brasil)):
    print(f'O estado {brasil[e]["uf"]} tem a sigla {brasil[e]["sigla"]}')
    
