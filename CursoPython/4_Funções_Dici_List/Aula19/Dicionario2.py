locadora = []

######### PARA DICIONÁRIOS USAR .ITEMS() E PARA LISTAS ENUMARETE

while True:
    filme = {
    'titulo' : str(input('Título: ')),
    'ano' : int(input('Ano: ')),
    'diretor' : str(input('Diretor: '))
    }
    locadora.append(filme.copy())
    filme.clear()
    fechar = int(input('\nDigite 1 para fechar: '))
    if fechar == 1:
        break

for i in range (0,len(locadora)):
    print(f'O {locadora[i]["titulo"]} é do ano {locadora[i]["ano"]} feito pelo direto {locadora[i]["diretor"]}') 

print('-='*25)
print(f'{"Título":<}  {"Ano":^30}  {"Diretor":>10}')
print('-'*50)
for i in range (0,len(locadora)):
    print(f'{locadora[i]["titulo"]:<}  {locadora[i]["ano"]:^30}   {locadora[i]["diretor"]:>10}')

print('-'*50)