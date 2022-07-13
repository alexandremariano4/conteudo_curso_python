pessoas = {'nome': 'Alexandre','sexo':'M', 'idade':22}
######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())

pessoas['nome'] = 'Carol'
pessoas['peso'] = '96'
print(pessoas)

for k,v in pessoas.items():
    print(f'{k} = {v}')