vel = int(input('Digite a velocidade que o carro está: '))
cores = {'limpa':'\033[m', 
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m'}
if vel > 80:
    print(f'{cores["vermelho"]}Você foi multado!{cores["limpa"]}')
    print('O valor da sua multa é de: R${}.00'.format((vel-80)*7))
else:
    print(f'{cores["verde"]}Você não foi multado!{cores["limpa"]}')
print('Dirija com segurança e bom dia!!')    

