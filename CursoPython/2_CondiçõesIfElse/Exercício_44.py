conta = float(input('Valor a ser pago: '))
opcao = int(input('Opção de pagamento: \n1-À vista\n2-À vista no cartão\n3-Em até 2x no cartão\n4-Em até 3x ou mais no cartão\n'))
if opcao == 1:
    print(f'Opção escolhida: À vista! (Desconto de 10%!)\nO valor a se pagar é de: R${conta*0.90}!')
elif opcao == 2:
    print(f'Opção escolhida: À vista no cartão (Desconto de 5%!)\nO valor a se pagar é de R${conta*0.95}!')
elif opcao == 3:
    print(f'Opção escolhida: Em até 2x no cartão (Sem desconto!)\nO valor a se pagar é de R${conta}!')
elif opcao == 4:
    print(f'Opção escolhida: Em até 3x ou mais no cartão (Juros de 20%!)\nO valor a se pagar é de R${conta*1.20}')
else:
    print('Digite uma opção válida')
    