print('{:=^30}'.format('COMPRA DE PRODUTOS'))
total = 0
prodCaro = 0
valorBarato = 0
nomeBarato = ''
cont = 0
while True:
    print('--'*30)
    cont += 1
    nProd = str(input('Digite o nome do produto: '))
    pProd = int(input('Qual o preço do produto: '))
    opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    total = total + pProd
    if cont == 1:
        valorBarato = pProd
    elif pProd < valorBarato:
        nomeBarato = nProd
        valorBarato = pProd
    if pProd > 1000:
        prodCaro += +1
    if opcao != 'S' or 'N':
        while opcao not in 'SsnN':
            opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print('--'*30)
print(f'O total gasto na compra foi: R${total}')    
print(f'{prodCaro} produtos custam mais de 1000.')
print(f'O nome do produto mais barato é {nomeBarato} e o seu valor é de {valorBarato}.')