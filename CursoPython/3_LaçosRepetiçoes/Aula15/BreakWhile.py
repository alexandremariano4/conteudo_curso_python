soma = 0
nome = 'Teste'
while True:
    print(f'{nome:->20}')
    print('{:-^20}'.format('Teste'))
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        break
    soma += n1
print('Acabou!')    