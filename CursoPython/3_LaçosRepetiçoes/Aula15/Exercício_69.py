print('{:=^30}'.format('Cadastro de Pessoas'))
maior = 0
qtH = 0
mul = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()[0]
    print('--'*30)
    opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    
    if opcao != 'S' and opcao != 'N':
        while opcao not in 'sSNn':
                opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]               
    if idade > 18:
        maior = maior +1   
    if sexo == 'M':
        qtH = qtH +1  
    if sexo == 'F' and idade < 20:
        mul = mul +1  
    if opcao == 'N':
        break 
print('--'*30)
print(f'Pessoas com mais de 18 anos {maior}.')
print(f'Homens cadastrados {qtH}.')
print(f'Mulheres com menos de 20 anos {mul}')