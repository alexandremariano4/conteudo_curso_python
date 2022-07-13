nome = str(input('Digite seu nome completo: ')).strip()

print('Têm "Silva" no seu nome? : ','silva' in nome.lower())
qtd = nome.lower().count('a')
print(f'A letra "A" aparece {qtd} no seu nome')
pos = nome.find('a')+1
print(f'A letra "A" aparece a primeira vez na posição {pos}')
print('A letra "A" aparece por último na posição: {}'.format(nome.rfind('a')+1))
