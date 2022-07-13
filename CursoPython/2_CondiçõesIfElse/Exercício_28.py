idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você tem {}{}{} anos, pode entrar!'.format('\033[1;32m', idade, '\033[m'))
elif idade < 18:
    print('Você tem {}{}{} anos, não pode entrar!!!'.format('\033[1;31m', idade, '\033[m'))