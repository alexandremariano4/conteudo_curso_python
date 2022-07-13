from typing import Type


def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try: 
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1= leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'Os números digitados foram {n1} e {n2}.')