from datetime import date

anoAtual = date.today().year


print('Digite seus dados de nascimento: ')

anoNasc = int(input('Ano: '))

idade = anoAtual - anoNasc

if idade <= 16:
    print(f'Você vai precisar se alistar! Faltam {18-idade} ano(s)')
elif idade == 18:
    print(f'Você precisa se alistar IMEDIATAMENTE!!!')
elif idade == 17:
    print(f'Você precisa se alistar daqui {18-idade} ano(s)')
else:
    print(f'Seu tempo de alistamento já passou!')
    