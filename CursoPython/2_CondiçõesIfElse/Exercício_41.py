from datetime import date
print('{:=^40}'.format(f'Confederação nacional de natação'))
ano = date.today().year

nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano - nascimento 
if idade <= 9:
    print(f'Você tem {idade} anos, você é um atleta MIRIM!')
elif idade >= 10 and idade <=14:
    print(f'Você tem {idade} anos, você é um atleta INFANTIL!')
elif idade >= 15 and idade <=19:
    print(f'Você tem {idade} anos, você é um atleta JUNIOR!!!')
elif 25 > idade >= 20:
    print(f'Você tem {idade} anos, vocÊ é um atleta SêNIOR!!!')
else:
    print(f'Você tem {idade} anos, você é um atleta MASTER!!!')

print('='*40)
