primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total  = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razão
        cont = cont +1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))


