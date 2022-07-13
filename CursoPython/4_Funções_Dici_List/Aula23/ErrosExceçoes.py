from decimal import DivisionByZero


try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError,DivisionByZero):
    print('Não é possível dividir um número por zero.')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados!!')
except Exception as error:
    print(f'O erro encontrado foi {error.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, Muito obrigado!')