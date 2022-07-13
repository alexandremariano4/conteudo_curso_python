salario = float(input('Digite seu salário: '))
if salario >= 1250.00:
    print(f'Parabéns, você recebeu um aumento de 10%! Seu novo salário é de {salario*1.10:.2f}')
else:
    print(f'Parabéns, você recebeu um aumento de 15%! Seu novo salário é de {salario*1.15:.2f}')