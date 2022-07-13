media = 0
velho = 0
qtdMulher = 0
guardaHomem = 'vazio'
guardaMulher = 'vazio'
for c in range (0,4):
    print('='*60)
    nome  = str(input(f'Digite o nome da {c+1}ª pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    sexo  = str(input(f'Digite o sexo da {c+1}ª pessoa: ')).strip()
    media = media + idade / 4 
    if sexo == 'f' or sexo == 'feminino' or sexo == 'F' or sexo == 'Feminino' :
        if idade < 20:
            qtdMulher = qtdMulher + 1
    guardaMulher = '' 
    if sexo == 'm' or sexo == 'masculino' or sexo == 'M'or sexo == 'Masculino':
        if idade > velho:
            velho = idade
            guardaHomem = nome 
print('='*60)   
if guardaHomem == 'vazio':
    print('Não tiveram homens na pesquisa!')
else:
    print(f'O homem mais velho tem {velho} anos e seu nome é {guardaHomem}!!!')
    
if guardaMulher == 'vazio':
    print('Não tiveram mulheres na pesquisa!')
else: 
    print(f'Existem {qtdMulher} mulheres com menos de 20 anos!!!')
print(f'A média de idade de todas pessoas é de {media}')
