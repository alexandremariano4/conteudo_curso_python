from time import sleep

cores = {'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'limpa':'\033[m'}

print('{:=^40}'.format(f'Empréstimo bancário'))

valor   = float(input('Digite o valor da casa: R$')) 
salario = float(input('Digite o salário de quem vai comprar: R$'))
anos    = int(input('Em quantos anos será pago: '))

print('='*40)

print(f'{cores["verde"]}CALCULANDO SEU EMPRÉSTIMO!!!{cores["limpa"]}')

sleep(2)

print(f'Serão {anos*12} meses pagando o empréstimo!!!')
sleep(1.5)
prestacao = valor / (anos*12)
print(f'Com prestações no valor de {prestacao:.2f}!')
sleep(2)

if prestacao > salario*0.30:
    print('='*40)
    print(f'{cores["vermelho"]}Temos uma má notícia...{cores["limpa"]}')
    sleep(1)
    print(f'30% do seu salário é: {salario*0.30}')
    print(f'Sua prestação por mês ficaria no valor de {cores["verde"]}{prestacao:.2f}{cores["limpa"]}, o que excederia o limite de 30% do seu salário de {cores["vermelho"]}{salario}{cores["limpa"]}, infelizmente não podemos oferecero empréstimo!')
    print('='*40)
else:
    print('='*40)
    print(f'{cores["verde"]}SUCESSO!!!{cores["limpa"]}')
    sleep(2)
    print(f'Seu empréstimo foi aprovado, suas prestações no valor de {prestacao:.2f} são menores do que 30% do seu salário ({prestacao:.2f}) de {salario} você poderá comprar uma casa nova!')
    print('='*40)
 